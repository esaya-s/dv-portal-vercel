import google.generativeai as genai
from django.conf import settings
from django.core.files.storage import default_storage
from PIL import Image, ImageEnhance
import io
import base64
import logging

logger = logging.getLogger(__name__)

class GeminiValidationService:
    """Gemini AI service for DV application validation"""
    
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro-vision')
            self.text_model = genai.GenerativeModel('gemini-pro')
        else:
            logger.warning("Gemini API key not configured")
            self.model = None
            self.text_model = None
    
    def validate_dv_photo(self, image_path):
        """Validate DV photo against US requirements using Gemini Vision"""
        if not self.model:
            return {
                'valid': False,
                'errors': ['AI validation service not configured']
            }
        
        try:
            # Load and process image
            image = Image.open(image_path)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Prepare prompt for DV photo validation
            prompt = """
You are an expert validator for US Diversity Visa (DV) program photos. Analyze this photo and check if it meets ALL the strict US DV photo requirements:

CRITICAL REQUIREMENTS TO CHECK:
1. WHITE BACKGROUND ONLY - Must be pure white, no shadows, patterns, or other colors
2. HEAD POSITION - Head must be directly facing camera, not tilted
3. EYES - Both eyes must be open and clearly visible
4. FACIAL EXPRESSION - Neutral expression, mouth closed, no smiling
5. HEAD SIZE - Head must be between 50-69% of image height
6. IMAGE QUALITY - Sharp, clear, in focus, no blur or pixelation
7. LIGHTING - Even lighting, no harsh shadows on face or background
8. CLOTHING - No uniforms, hats, or head coverings (except religious)
9. GLASSES - If worn, no glare, frames not obscuring eyes
10. IMAGE FORMAT - Square format (1:1 ratio)
11. RECENT PHOTO - Must appear to be a recent photo
12. NO EDITING - No obvious photo manipulation or filters

RETURN YOUR ANALYSIS AS:
VALID: [YES/NO]
BACKGROUND: [PASS/FAIL] - Brief explanation
HEAD_POSITION: [PASS/FAIL] - Brief explanation  
EYES: [PASS/FAIL] - Brief explanation
EXPRESSION: [PASS/FAIL] - Brief explanation
HEAD_SIZE: [PASS/FAIL] - Brief explanation
QUALITY: [PASS/FAIL] - Brief explanation
LIGHTING: [PASS/FAIL] - Brief explanation
OVERALL_ASSESSMENT: [Detailed explanation of why photo passes or fails]

Be extremely strict - even minor violations should result in FAIL.
            """
            
            response = self.model.generate_content([prompt, image])
            analysis = response.text
            
            # Parse response
            validation_result = self._parse_photo_validation(analysis)
            
            return validation_result
            
        except Exception as e:
            logger.error(f"Error validating DV photo: {e}")
            return {
                'valid': False,
                'errors': [f'Photo validation error: {str(e)}']
            }
    
    def validate_application_data(self, application_data):
        """Validate application data for completeness and accuracy"""
        if not self.text_model:
            return {
                'valid': False,
                'errors': ['AI validation service not configured']
            }
        
        try:
            prompt = f"""
You are an expert validator for US Diversity Visa (DV) applications. Review this application data and check for:

APPLICATION DATA:
{self._format_application_data(application_data)}

CHECK FOR:
1. COMPLETENESS - All required fields filled
2. CONSISTENCY - Information matches across fields
3. ELIGIBILITY - Basic DV eligibility requirements
4. DATA QUALITY - Names, dates, addresses look realistic
5. COUNTRY ELIGIBILITY - Country of birth eligible for DV program
6. EDUCATION/WORK - Meets minimum requirements
7. DATES LOGIC - Birth date, marriage dates, etc. make sense
8. NAME FORMATTING - Proper capitalization and formatting

SPECIFIC VALIDATION RULES:
- Must be born in DV-eligible country
- Must have high school education or 2+ years work experience
- Age must be reasonable (18+ typically)
- Marital status must match spouse/children data
- All names should be properly formatted
- Addresses should be complete and realistic
- Phone numbers should match country format

RETURN ANALYSIS AS:
VALID: [YES/NO]
ELIGIBILITY: [PASS/FAIL] - Country and basic requirements
COMPLETENESS: [PASS/FAIL] - All fields properly filled
CONSISTENCY: [PASS/FAIL] - Data matches across fields
DATA_QUALITY: [PASS/FAIL] - Information appears accurate
ERRORS: [List any specific errors found]
WARNINGS: [List any concerns or suggestions]
RECOMMENDATIONS: [Suggestions for improvement]

Be thorough but helpful in your analysis.
            """
            
            response = self.text_model.generate_content(prompt)
            analysis = response.text
            
            # Parse response
            validation_result = self._parse_application_validation(analysis)
            
            return validation_result
            
        except Exception as e:
            logger.error(f"Error validating application data: {e}")
            return {
                'valid': False,
                'errors': [f'Application validation error: {str(e)}']
            }
    
    def validate_spouse_children_photos(self, spouse_photo=None, children_photos=None):
        """Validate spouse and children photos"""
        results = {}
        
        if spouse_photo:
            results['spouse'] = self.validate_dv_photo(spouse_photo)
        
        if children_photos:
            results['children'] = []
            for i, child_photo in enumerate(children_photos):
                child_result = self.validate_dv_photo(child_photo)
                child_result['child_index'] = i + 1
                results['children'].append(child_result)
        
        return results
    
    def _format_application_data(self, data):
        """Format application data for AI analysis"""
        formatted_data = []
        
        # Basic personal info
        if hasattr(data, 'first_name'):
            formatted_data.append(f"Name: {data.first_name} {data.middle_name or ''} {data.last_name}")
            formatted_data.append(f"Gender: {data.gender}")
            formatted_data.append(f"Date of Birth: {data.date_of_birth}")
            formatted_data.append(f"Country of Birth: {data.country_of_birth}")
            formatted_data.append(f"City of Birth: {data.city_of_birth}")
            formatted_data.append(f"Current Country: {data.current_country}")
            formatted_data.append(f"Education: {data.education_level}")
            formatted_data.append(f"Occupation: {data.occupation}")
            formatted_data.append(f"Marital Status: {data.marital_status}")
            formatted_data.append(f"Email: {data.email}")
            formatted_data.append(f"Phone: {data.phone_number}")
        
        return "\n".join(formatted_data)
    
    def _parse_photo_validation(self, analysis_text):
        """Parse Gemini photo validation response"""
        lines = analysis_text.split('\n')
        result = {
            'valid': False,
            'details': {},
            'errors': [],
            'warnings': []
        }
        
        for line in lines:
            line = line.strip()
            if line.startswith('VALID:'):
                result['valid'] = 'YES' in line.upper()
            elif ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key in ['background', 'head_position', 'eyes', 'expression', 'head_size', 'quality', 'lighting']:
                    result['details'][key] = value
                    if 'FAIL' in value.upper():
                        result['errors'].append(f"{key.replace('_', ' ').title()}: {value}")
                elif key == 'overall_assessment':
                    result['overall_assessment'] = value
        
        return result
    
    def _parse_application_validation(self, analysis_text):
        """Parse Gemini application validation response"""
        lines = analysis_text.split('\n')
        result = {
            'valid': False,
            'details': {},
            'errors': [],
            'warnings': [],
            'recommendations': []
        }
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('VALID:'):
                result['valid'] = 'YES' in line.upper()
            elif line.startswith('ERRORS:'):
                current_section = 'errors'
            elif line.startswith('WARNINGS:'):
                current_section = 'warnings'
            elif line.startswith('RECOMMENDATIONS:'):
                current_section = 'recommendations'
            elif ':' in line and current_section is None:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                result['details'][key] = value
            elif line.startswith('-') or line.startswith('•'):
                if current_section:
                    result[current_section].append(line[1:].strip())
            elif line and current_section:
                result[current_section].append(line)
        
        return result
    
    def generate_success_tips(self, application_data):
        """Generate personalized tips for DV success"""
        if not self.text_model:
            return "AI tips service not available"
        
        try:
            prompt = f"""
Based on this DV application data, provide helpful and encouraging tips for maximizing chances of success:

{self._format_application_data(application_data)}

Provide 5-7 specific, actionable tips including:
1. Document preparation advice
2. Interview preparation (if selected)
3. Common mistakes to avoid
4. Timeline expectations
5. Additional requirements they should be aware of

Make the response encouraging and professional. Focus on what they CAN do to improve their chances.
            """
            
            response = self.text_model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            logger.error(f"Error generating tips: {e}")
            return "Unable to generate personalized tips at this time."

# Global service instance
gemini_service = GeminiValidationService()

# Helper functions
def validate_dv_photo(image_path):
    """Validate DV photo using Gemini AI"""
    return gemini_service.validate_dv_photo(image_path)

def validate_application(application):
    """Validate full application using Gemini AI"""
    return gemini_service.validate_application_data(application)

def validate_family_photos(spouse_photo=None, children_photos=None):
    """Validate spouse and children photos"""
    return gemini_service.validate_spouse_children_photos(spouse_photo, children_photos)

def get_success_tips(application):
    """Get personalized success tips"""
    return gemini_service.generate_success_tips(application)
