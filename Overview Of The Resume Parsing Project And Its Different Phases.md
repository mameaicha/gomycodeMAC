# Overview of the resume parsing project and its different phases



### Introduction

In the past, corporate HR managers spent a lot of time analyzing CVs to find the ideal profile for a given recruitment. But now with resume parser there has been a considerable improvement in their recruitment process.

Resume parsing refers to the automated storage, organization and analysis of job resumes. Resume parsers analyze a resume, extract the desired information, and insert the information into a database with a unique entry for each candidate. Once the resume has been analyzed, a recruiter can search the database for keywords and phrases and get a list of relevant candidates.

The main objective of this project is to implement a  resume parser programme.

### Different technologies that were used  in resume parser 

Resume parsing technology typically uses a combination of natural language processing (NLP) and machine learning techniques to extract and structure information from resumes and CVs.

NLP is a field of artificial intelligence that deals with the interaction between computers and human languages. It involves using algorithms and machine learning models to process and analyze natural language text, such as resumes and CVs, and extract meaning from it.

Machine learning is a type of artificial intelligence that enables computers to learn and make decisions without being explicitly programmed. In the context of resume parsing, machine learning algorithms can be trained to recognize patterns and structure in resumes and CVs and use this information to extract and structure the relevant data.

Other technologies that may be used in resume parsing include:

- **Optical character recognition (OCR)**: This technology is used to convert scanned documents or images of text into machine-readable text. It can be useful for parsing resumes and CVs that are not in electronic format.

- Python libraries **SpaCy**: SpaCy is a free, open-source software library for advanced natural language processing (NLP), written in the programming languages Python and Cython. It’s designed specifically for production use and helps you build applications that process and “understand” large volumes of text.  It features state-of-the-art speed and neural network models for tagging, parsing, named entity recognition**, **text classification and more. It can be used to build information extraction or natural language understanding systems. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.

- Database management: Many resume parsers use a database to store the extracted information in a structured format.  This can allow recruiters and hiring managers to search and filter the data to identify qualified candidates.  In this project we use **SQL Server Management Studio** ( *SSMS* ) 

  

### Different phases of the project

This project will be carried out in stages.

1. **The first stage**, known as the **data extraction phase**:

   Information extraction  involves extracting meaningful information from unstructured textual data and presenting it in a structured format. Information extraction makes it possible to retrieve predefined information such as the name of a person, the location of an organization, or to identify a relationship between entities, and to save this information in a structured format such as a database.

   To do this :

   - we search for a collection of CVs in different formats (pdf, image and world).  We found  a resume dataset in https://www.kaggle.com/datasets/shivani12sharma/resume-dataset-new and in https://www.kaggle.com/datasets/palaksood97/resume-dataset and download its.

   - We extract the relevant information from the resumes in a structured format that can be used for further processing.

     - For PDF resumes, we use **PyPDF2** to extract  extracts text from it.

     - For images resumes, we load the resume image using **OpenCV**, we converts the image to grayscale, and then uses **pytesseract** to perform Optical Character Recognition (OCR) and extract text from the image.

     - For resumes in a docx format, we extracts text from the document using the **docx library**.

       Below is a code extract from this phase
       
       ```python
       #extract_text_from_pdf: This function takes a PDF or  file path as input and extracts text from all the pages in the PDF using PyPDF2
       
       def extract_text_from_pdf(pdf_path):
           with open(pdf_path, 'rb') as file:
               pdf_reader = PyPDF2.PdfReader(file)
               text = ''
               for page in pdf_reader.pages:
                   text += page.extract_text()
               text = text.strip()
               text = ' '.join(text.split())
           return text
       
       
       #extract_text_from_image: This function takes an image file path as input, converts the image to grayscale, and then uses pytesseract to perform Optical Character Recognition (OCR) and extract text from the image.
       # #Load the resume image using OpenCV and use OCR to extract text from the image
       def extract_text_from_image(image_path):
           # Load the image using OpenCV
           image = cv2.imread(image_path)
           # Convert the image to grayscale
           gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
           # Perform OCR to extract text
           text = pytesseract.image_to_string(gray)
           text = text.strip()
           text = ' '.join(text.split())
           return text
       
       #extract_text_from_docx: This function takes a DOCX file path as input and extracts text from the document using the docx library.
       def extract_text_from_docx(docx_path):
           doc = docx.Document(docx_path)
           text = '\n'.join([para.text for para in doc.paragraphs])
           text = text.strip()
           text = ' '.join(text.split())
           return text
       
       ```
     
     
     
     After, then the text is pre-processed to extract the relevant information such as name, email, phone number, education details, work experience, skills, etc. by using python libraries SpaCy.
     
     Below is a code extract from this phase
     
     ```python
     #Contact information
     
     def extract_name_from_resume(resume_text):
         nlp = spacy.load('en_core_web_sm')
         matcher = Matcher(nlp.vocab)
     
         # Define name patterns
         patterns = [
             [{'POS': 'PROPN'}, {'POS': 'PROPN'}],  # First name and Last name
             [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],  # First name, Middle name, and Last name
             [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]  # First name, Middle name, Middle name, and Last name
             # Add more patterns as needed
         ]
     
         for pattern in patterns:
             matcher.add('NAME', patterns=[pattern])
     
         doc = nlp(resume_text)
         matches = matcher(doc)
     
         for match_id, start, end in matches:
             span = doc[start:end]
             return span.text
     
         return None
     
     
     def extract_contact_number_from_resume(text):
         contact_number = None
     
         # Use regex pattern to find a potential contact number
         pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
         match = re.search(pattern, text)
         if match:
             contact_number = match.group()
     
         return contact_number
     
     def extract_email_from_resume(text):
         email = None
     
         # Use regex pattern to find a potential email address
         pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
         match = re.search(pattern, text)
         if match:
             email = match.group()
     
         return email
     
     def extract_skills_from_resume(text, skills_list):
         skills = []
     
         for skill in skills_list:
             pattern = r"\b{}\b".format(re.escape(skill))
             match = re.search(pattern, text, re.IGNORECASE)
             if match:
                 skills.append(skill)
     
         return skills
     
     # Education
     def extract_education_from_resume(text):
         education = []
     
         # Use regex pattern to find education information
         pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
         matches = re.findall(pattern, text)
         for match in matches:
             education.append(match.strip())
     
         return education
     
     
     # Function to perform Aptitude extraction using RAKE
     def extract_Aptitude_frome_resume(text):
         r = Rake(min_length=2, max_length=4)  # Adjust min_length and max_length as needed
         r.extract_keywords_from_text(text)
         ranked_phrases = r.get_ranked_phrases()
         # Additional stop words specific to resumes that we want to exclude
         STOPWORDS = [
         'resume', 'cv', 'summary', 'experience', 'education', 'skill', 'skills', 'abilities', 'project', 'projects',
         'work', 'worked', 'company', 'companies', 'responsibilities', 'responsibility', 'achieved', 'team', 'teams']
         ap = [phrase for phrase in ranked_phrases if not any(stopword in phrase.lower() for stopword in STOPWORDS)]
         return ap
     
     
     
     ```

   

2. **Phase II**, known as the **Data Cleaning** phase, consists  of 

   To ensure that the extracted data is consistent and free from errors and consistent.

   In this phase, the extracted data is cleaned and normalized by removing noise, formatting inconsistencies, and Irrelevant information.

   Below is a code extract from this phase

   ```python
   def preprocess(txt):
       # convert all characters in the string to lower case
       txt = txt.lower()
       # remove non-english characters, punctuation and numbers
       txt = re.sub('[^a-zA-Z]', ' ', txt)
       txt = re.sub('http\S+\s*', ' ', txt)  # remove URLs
       txt = re.sub('RT|cc', ' ', txt)  # remove RT and cc
       txt = re.sub('#\S+', '', txt)  # remove hashtags
       txt = re.sub('@\S+', '  ', txt)  # remove mentions
       txt = re.sub('\s+', ' ', txt)  # remove extra whitespace
       # tokenize word
       txt = nltk.tokenize.word_tokenize(txt)
       # remove stop words
       txt = [w for w in txt if not w in nltk.corpus.stopwords.words('english')]
       
   
       return ' '.join(txt)
   ```

   

3. **Phase III**, known as the **entity recognition** phase, consists  of 

   

   - **Categorize the entities into different types, such as names, organizations, locations, dates, and so on**.

     The relevant entities are recognized in this phase using named entity recognition (NER) techniques. Named-entity recognition is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. The entities can be categorized into different types, such as names, organizations, locations, dates, and so on.

     Below is a code extract from this phase

     ```python
     #Use spaCy to parse the resume and perform NER to identify named entities.
     def parse_resume(resume_text):
         # Parse the resume text using spaCy
         doc = nlp(resume_text)
     
         # Extract named entities
         named_entities = [(ent.text, ent.label_) for ent in doc.ents]
     
         return named_entities
         
     
     #categorize the entities into different types (e.g., names, organizations, locations, dates), you can filter the named entities based on their entity types
     def categorize_entities(named_entities):
         entity_categories = {
             'person': [],
             'organization': [],
             'location': [],
             'date': [],
             'other': []
         }
         
         for entity, entity_type in named_entities:
             if entity_type == 'PERSON':
                 entity_categories['person'].append(entity)
             elif entity_type == 'ORG':
                 entity_categories['organization'].append(entity)
             elif entity_type == 'LOC':
                 entity_categories['location'].append(entity)
             elif entity_type == 'DATE':
                 entity_categories['date'].append(entity)
             else:
                 entity_categories['other'].append(entity)
         
         return entity_categories
     ```

     In this step, we note that there are some cathegorization errors.

     As the models are statistical and depend heavily on the examples on which they have been trained, this doesn't always work perfectly and may require further adjustments, depending on your use case.

     This is why, we must first train our spacy model on manually labeled data and create a customized NER. So first we need to train our spacy model on manually labeled CV data. For training purposes, we obtained data online.

     

   - **Training custom NER models using labeled data**

     To improve this, we need to update and train the NER according to context and requirements.
     To do this, we need to

     - use a pre-trained spacy model.

     - provide training examples that will enable the NER to learn for future samples.

       we download training examples data in https://www.kaggle.com/code/mohamedtaha7/ner-on-resumes-using-spacy/input?select=Entity+Recognition+in+Resumes.json

     - Configuring Spacy:

       This step involves configuring SpaCy for your custom NER model involves initializing configuration files, and you can use a base configuration file as a template. To download the base_config.cfg file from the documentation, you can visit the official spaCy documentation website:

       spaCy base_config.cfg

       Download the file by clicking on the bottom-right download button present the command shell itself.

       This file serves as a starting point for creating your custom configuration tailored to your specific NER model training. We use the base_config.cfg as a template to create our custom config.cfg.

     - Defining the Data Processing Function

       The provided code defines a function that is used to create spaCy DocBin objects from annotated data. This function plays a crucial role in the process of preparing data for training custom Named Entity Recognition (NER) models. Let’s break down the importance and functionality of this code:

       Why it is needed:

       - **Data Preparation**: In NER tasks, having properly formatted training data is essential. This data typically consists of text documents with labeled entities, where each entity is defined by its start and end positions in the text and its associated label (e.g., person, organization, date).

       - **SpaCy Integration**: spaCy is a popular NLP library that offers robust capabilities for NER model training. To leverage spaCy for training, you need to convert your annotated data into a format that spaCy understands.

         This step includes

         - **Conversion to spaCy Format**: It transforms annotated data into a format compatible with spaCy v3, creating Doc objects with character spans linked to entities.

         - **Entity Alignment**: Prevents entity overlaps or conflicts within documents, avoiding training issues.

         - **Error Logging**: Captures and logs data issues, aiding debugging and data quality assessment.

         - **Efficient Data Loading**: Utilizes spaCy’s DocBin for efficient storage and loading of processed documents, crucial for managing large datasets during model training.

           

       - **Splitting and DocBin Creation**:

         In this section, we split the annotated data into training and testing sets, display their sizes, and create spaCy DocBin objects for both sets. Additionally, we log errors during the annotation processing.

       - Model Training:

       - Model Testing:

         

4.  **Phase IV**: called the **relationship extraction**   phase

   Once the entities are identified, the relationships between them are extracted. For example, the relationship between a person's name and SKILLS can be extracted.

   Below is a code extract from this phase

   ```python
   doc = nlp_ner(resume_text1)
   #Extract Relationships:
   relationships = []
   
   for ent1 in doc.ents:
       for ent2 in doc.ents:
           if  ent1.label_.upper() == "NAME" and ent2.label_.upper() == "COMPANIES WORKED AT" and ent1.start < ent2.start:
               relationships.append((ent1.text, ent2.text))
   
   #Display the Relationships:
   for relationship in relationships:
       print(f"{relationship[0]} is a {relationship[1]}")
   ```

5.  **Phase V**: called **Data integration and model creation** phase

    In this phase, extracted information is integrated into a structured format and stored in a database or spreadsheet for further analysis.

   In this step we use **SQL Server Management Studio** ( *SSMS* ) 

   Below is a code extract from this phase

   ```sql
   -- Drop the table if it already exists
   IF OBJECT_ID('personne', 'U') IS NOT NULL
   DROP TABLE personne
   GO
   -- Create the table personne
   CREATE TABLE personne
   (
       personneId INT NOT NULL PRIMARY KEY, -- primary key column
       personneName VARCHAR(100) NOT NULL,
       email VARCHAR(100),
   );
   GO
   
   -- Drop the table if it already exists
   IF OBJECT_ID('education', 'U') IS NOT NULL
   DROP TABLE education 
   GO
   
   
   -- Create the table education
   CREATE TABLE education (
   	educationId  INT NOT NULL PRIMARY KEY,
       personneId INT FOREIGN KEY REFERENCES personne(personneId),
   	degree TEXT,
   	schoolOrUniversity	TEXT,
       graduationYearn DATE
   );
   GO
   
   -- Drop the table if it already exists
   IF OBJECT_ID('workExperience', 'U') IS NOT NULL
   DROP TABLE workExperience 
   GO
   
   -- Create the table workExperience
   CREATE TABLE workExperience (
   	workExperienceId  INT NOT NULL PRIMARY KEY,
       personneId INT FOREIGN KEY REFERENCES personne(personneId),
   	--jobTitle VARCHAR(150) NOT NULL,
       yearsofExperience  INT,
   	companiesWorkedAt	TEXT,
       ---startingDate DATE,
       ----dateOfEnd DATE,
       ---dutiesAndResponsibilities TEXT,
   );
   GO
   
   -- Drop the table if it already exists
   IF OBJECT_ID('skills', 'U') IS NOT NULL
   DROP TABLE skills 
   GO
   
   -- Create the table workExperience
   CREATE TABLE skills (
   	skillsId  INT NOT NULL PRIMARY KEY,
       personneId INT FOREIGN KEY REFERENCES personne(personneId),
       relevantSkills TEXT,
   	---technicalSkills VARCHAR(150) NOT NULL,
   	---languageProficiency	TEXT,
       ---otherRelevantSkills TEXT,
       
   );
   GO
   
   
   -- Drop the table if it already exists
   IF OBJECT_ID('otherFields', 'U') IS NOT NULL
   DROP TABLE otherFields
   GO
   
   -- Create the table workExperience
   CREATE TABLE otherFields (
   	otherFieldsId  INT NOT NULL PRIMARY KEY,
       personneId INT FOREIGN KEY REFERENCES personne(personneId),
   	location1 TEXT ,
       Designation TEXT ,
       other TEXT ,
   	---languageProficiency	TEXT,
       otherRelevantSkills TEXT,
       skills TEXT,
   );
   GO
   ```

## Conclusion

Extract the required candidate information without manually scanning each CV. This can save recruiters a lot of time and effort, and it can also help ensure that all relevant information is captured in every CV. This can be achieved thanks to resume parser.

The aim of this project was to implement a resume parser using python's OCR and Spacy tools.

This project was carried out in several phases: data extraction, data cleansing, entity recognition, relationship extraction and data integration and model creation.

The main difficulty encountered is obtaining quality data (CVs).

