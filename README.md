# SeizureSafeguard: A Wearable IoT Device for Real-Time Epileptic Seizure Detection

By
\
Aitijhya Sarkar, Roll No. 10900120121
\
Ankit Chowdhury, Roll No. 10900120145
\
Nilanjana Sarkar, Roll No. 10900121226
\
Rishmita Sen, Roll No. 10900121222
\
\
Under the guidance of
\
Prof. Arnab Chakraborty


\
**Table of Contents**
- [1. Abstruct](#1-abstruct)
- [2. Introduction](#2-introduction)
	- [2.1. Background and Significance of Epilepsy Detection using EEG](#21-background-and-significance-of-epilepsy-detection-using-eeg)
	- [2.2. Objectives](#22-objectives)
	- [2.3 Scope and Limitations](#23-scope-and-limitations)
- [3. Literature Survey](#3-literature-survey)
- [4. Proposed Work](#4-proposed-work)
	- [4.1 Project Implementation](#41-project-implementation)
	- [4.2 Ethical Considerations](#42-ethical-considerations)
- [5. Epileptic Case Study](#5-epileptic-case-study)
- [6. Symptoms of Epilepsy](#6-symptoms-of-epilepsy)
- [7. Breif Description of Epilesy](#7-breif-description-of-epilesy)
- [8. Types of Epileptic Seiures](#8-types-of-epileptic-seiures)
- [9. Epilepsy recent trends and data](#9-epilepsy-recent-trends-and-data)
- [10. Need of EEG](#10-need-of-eeg)
- [11. How EEG works in detecting epilepsy](#11-how-eeg-works-in-detecting-epilepsy)
- [12. Existing Devices](#12-existing-devices)
	- [12.1 SEIZALARM](#121-seizalarm)
 	- [12.2 EMBRACE 2](#122-embrace-2)
- [13. Our Differentiating Factor](#13-our-differentiating-factor)
- [14. Future Scope of Our Project](#14-future-scope-of-our-project)
- [15. Conclusion](#15-conclusion)

## 1. Abstruct   

This project aims to develop a wearable device that can detect seizures in epileptic patients through the real-time analysis of patient parameters such as EEG, heart rate, temperature,  and  involuntary  jerking  motions.  The  physiological  data  will  be continuously  monitored  and  recorded  using  sensors  embedded  in  a  wristband. Collected data will then be analysed using machine learning algorithms to detect abnormal patterns indicating the onset of a seizure. Once a seizure is detected, the device will alert caregivers or medical professionals on a connected mobile app. This project is expected to significantly improve the quality of life for epileptic patients by providing timely and accurate detection of seizures, allowing for prompt medical intervention. A log will be maintained enabling healthcare professionals to monitor patient progress and adjust treatment plans accordingly. The use of IoT technology in this project represents a promising advancement in the field of healthcare and has the potential to greatly benefit patients with epilepsy.

## 2. Introduction   

Epilepsy, a chronic noncommunicable neurodegenerative disorder, affects 50 million people of all ages worldwide. [1](https://www.who.int/news-room/fact-sheets/detail/epilepsy) It  is  characterised by recurrent  seizures  caused by abnormal  electrical discharges in the cerebral region of the brain.
A person with epilepsy has two or more unprovoked seizures that happen more than twenty-four hours apart. Depending on which areas of the brain are affected, an excessive spike in electrical activity in the brain during a seizure can result in a wide range of symptoms.
Seizures can be broadly classified into three categories: generalised, focal, and epileptic spasms.

### 2.1. Background and Significance of Epilepsy Detection using EEG

Epilepsy detection using EEG is a valuable technique that involves recording and analysing the electrical activity in the brain. This method helps doctors diagnose epilepsy and understand the pattern and characteristics of seizures. By studying the EEG signals, healthcare professionals can identify abnormal brain activity and determine the type and severity of epilepsy. This information is  crucial  for  prescribing  appropriate  medications,  implementing  treatment  strategies,  and improving the overall management of epilepsy. It allows for a more precise and personalised approach to care, ultimately enhancing the quality of life for individuals living with epilepsy. EEG allows detection of a large spectrum of seizure types, even those without motor and autonomic features.[2](https://doi.org/10.1016/s1474-4422(18)30034-6)
The EEG signal of an epileptic patient can be segmented into four sections, namely pre-ictal (before seizure), ictal (during seizure), post-ictal (after seizure) and inter-ictal (between seizure episodes). The pre-ictal and inter-ictal stages are key sections in predicting seizure onset.[3](https://doi.org/10.1016/j.bbe.2021.01.006)

![image](https://github.com/aitijhyasarkar/SeizureSafeguard/assets/91305796/8425231f-500c-4fd4-b07f-6e435035638b)
\
**Figure 1:** EEG waves in General Tonic Clonic Seizure [4](https://www.ncbi.nlm.nih.gov/books/NBK390354/)

![image](https://github.com/aitijhyasarkar/SeizureSafeguard/assets/91305796/9cd8212f-400f-469d-a003-2f619a09851e)
\
Postictal: Period shortly after the seizure.
Interictal: Period between seizures, excluding the above periods.
\
**Figure 2:** An example of signals during a seizure with definitions of the definitions of the different periods [5](https://doi.org/10.1007/s11265-021-01659-x)

### 2.2. Objectives
In our project, we aim to create an automated system for seizure detection using IoT. The objective is to develop a device that can continuously monitor and analyse various physiological signals and movement patterns in individuals with epilepsy. By leveraging IoT technologies such as wearable devices or sensors, the system will collect real-time data from these individuals. This data will then be processed and analysed using advanced machine learning algorithms. The system will be trained to recognize specific patterns or changes in the collected data that indicate the occurrence of a seizure. Once a seizure is detected, the system will generate timely alerts to notify caregivers or medical professionals. This will allow for immediate intervention and assistance, potentially reducing the risk of injury or complications during a seizure.
Seizure  detection  devices  also  allow  objective  tracking  of  frequency  of  seizures,  allowing healthcare professionals to evaluate response to therapy and appropriately adjust medications. [6](https://doi.org/10.1016/j.jns.2021.117611)

### 2.3 Scope and Limitations

The scope of this project involves developing an automated system for seizure detection using IoT technologies. This system will aim to continuously monitor and analyse various physiological signals and movement patterns in individuals with epilepsy. By leveraging IoT devices such as wearable sensors, the system will collect real-time data from these individuals. The focus will be on utilising advanced, power-efficient algorithms and machine learning techniques to analyse this data and accurately detect seizures. The system will then generate timely alerts to notify caregivers or medical professionals, enabling them to provide immediate support and intervention during seizure episodes.
As for the limitations, the accuracy of seizure detection can vary based on individual differences in symptoms and seizure patterns. The system may not be able to detect all seizures accurately due to the complexity and variability of seizure episodes. Additionally, external factors such as environmental noise or interference may affect the system's performance. The performance of EEG-based seizure detection devices decreases with reduction in the number of electrodes. [7](https://doi.org/10.1111/epi.14052) There is also the problem of false alarms. Building a generic method that would fit for every epileptic patient is a tedious task, owing to the fact that epileptic seizure pattern in one patient may be a normal EEG in another patient. [8](https://doi.org/10.1007/s11036-018-1113-0)

## 3. Literature Survey

Traditionally, scalp EEG has been used in diagnosis, detection and classification of epileptic seizures. But this method is typically complex, and in some cases, prone to false alarms and limited sensitivity.  Seizure detection devices make use of various sensors ranging  from  movement detectors like electromyography, accelerometers, gyroscope, autonomic change detectors like heart rate, body temperature, blood pressure, oxygen saturation, and EEG surface electrodes apart from Near Infrared Spectroscopy. 
Most commercially available in-home seizure detection devices rely on heart rate and/or bed movement. A lot of these devices have not received due regulatory approval from medical bodies. Almost all seizure detection devices are designed to detect only tonic-clonic seizures. Ongoing studies give hope on using heart rate variability as a reliable indicator. [9](https://doi.org/10.1111/epi.16555) 
The pressing issue is that epileptic patients need fast and quality healthcare. Seizures can cause mild to serious injuries, concussions, or even Sudden Unexpected Death in Epilepsy (SUDEP) in case there is any delay in getting medical attention. [10](https://doi.org/10.1053/spen.2001.29476) Therefore, a Wearable IoT Device for Real-Time Epileptic Seizure Detection is required for timely medical attention and preventing life- threatening conditions like paralysis, permanent brain damage, or in rare cases, death. [11](https://www.hopkinsmedicine.org/health/conditions-and-diseases/status-epilepticus)

## 4. Proposed Work

Our proposed work centres around the development and implementation of a groundbreaking wearable  device  engineered  for  continuous  monitoring  and  real-time  detection  of  epileptic seizures. Each key feature of the device is meticulously designed to enhance user experience and provide a comprehensive solution to seizure management.
- **Wearable EEG Monitoring:**
The device boasts the integration of a lightweight and comfortable EEG sensor in a compact form factor, ensuring uninterrupted monitoring of the user's brain activity. This design consideration prioritises user comfort, promoting prolonged and consistent usage of the device.
- **Real-time Seizure Detection:**
To enable swift intervention, advanced signal processing algorithms are employed for the real-time analysis of EEG signals. These algorithms have been fine-tuned to detect subtle patterns indicative of epileptic seizures, ensuring timely alerts to caregivers or medical professionals.
- **Alerting Mechanism:**
A robust alerting mechanism is integral to the device, featuring visual cues through a display, haptic feedback via vibration, and audible alerts through a small speaker upon seizure detection. This multi-sensory approach aims to promptly capture the attention of the user and those around them.
- **Automatic Message Sending:**
Our device is equipped with a communication module that automates the sending of pre- configured alert messages to a predefined list of emergency contacts or caregivers. This feature ensures that crucial information reaches the necessary individuals without delay.
- **Location Services:**
Enhancing emergency response, the device integrates GPS or other location services to include precise information about the user's location in the alert messages. This assists responders in reaching the user quickly, optimising the effectiveness of the emergency intervention.
- **User-Friendly Interface:**
The  device  prioritises  an  intuitive  user  interface,  providing  real-time  EEG  data, customizable alert settings, and battery status. This user-centric design aims to facilitate ease of use and seamless interaction with the device.
- **Mobile App Integration:**
A companion mobile application is developed to complement the device, allowing users to customise alert settings, visualise historical seizure data, and manage emergency contacts. This integration provides users with a comprehensive tool for monitoring and managing their epilepsy.
- **Power Efficiency:**
Efficient power management is at the forefront of the device's design, incorporating features such as automatic sleep modes during inactive monitoring periods. This ensures an extended battery life, minimising disruptions in monitoring due to frequent recharging.

### 4.1 Project Implementation

The implementation of the device involves a synergistic combination of embedded systems, signal processing techniques, and wireless communication technologies. The device processes EEG data locally, and upon seizure detection, it seamlessly communicates with the paired mobile app to trigger alerts, ensuring a swift and efficient response to potential seizure episodes.

![image](https://github.com/aitijhyasarkar/SeizureSafeguard/assets/91305796/a5dddb24-1041-49ac-a139-9ff1bb3cacf9)
\
Figure 3: A block diagram of epileptic seizure detection using EEG signals and machine/deep learning techniques. [12](https://doi.org/10.1155/2022/6486570)

### 4.2 Ethical Considerations

Privacy and security are paramount in the implementation of the device, it strictly adheres to all relevant privacy regulations to safeguard the user's sensitive health data. Informed consent and user education are integral components of the deployment process, ensuring users are fully aware of how their data is utilised and upholding ethical standards in the utilisation of health-related information.
Our proposed work not only emphasises technological innovation in seizure detection but also places a significant emphasis on user-centric design, ethical considerations, and privacy protection to ensure a holistic and responsible approach to healthcare technology development.

## 5. Epileptic Case Study

Rita, a 13-year-old girl, experienced her first seizure in June 2013 while suffering from a high fever in Kolkata, India.
Teeth bonded for ten to fifteen seconds, causing weakness, unconsciousness, and blurred vision.
Under the care of a neurologist who prescribed generic medications Second seizure in Kolkata on July 16, 2017, at 18:00 IST
After being brought to a nearby nursing home, the patient received injections of phenytoin, normal saline, and steroids.
Admitted for four days, during which time they had blood, stool, chest, and EEG tests.
Diagnosis: Myoclonic seizures, juvenile myoclonic epilepsy, primary generalised tonic-clonic seizures, probable onset seizures with or without generalisation, and idiopathic generalised epilepsy.
Levetiracetam prescribed (LEVERA 500MG TABLET)

## 6. Symptoms of Epilepsy

Seizures are abrupt, uncontrollable electrical disruptions in the brain that can take on a variety of forms. Loss of Consciousness: During a seizure, some people may experience a loss of awareness or consciousness.
Jerking Movements: Seizures are frequently accompanied by jerking movements or involuntary muscle contractions.
Periods of inaction or blank staring are known as staring spells.
Temporary Confusion: Following a seizure, people may feel lost or confused.
Fatigue: Experiencing seizures can be mentally and physically taxing.
Headache: In certain situations, headaches or migraines may occur after a seizure.
Sleep disturbances can result from seizures, which can interfere with regular sleep cycles.
Grand mal seizures, also referred to as tonic-clonic movements, are typified by jerky movements that are followed by a stiffening of the muscles.

## 7. Breif Description of Epilesy

- A brain-related neurological disorder called epilepsy increases a person's risk of experiencing frequent , spontaneous seizures. It is one of the most widespread 
ner vous system disorders, affecting individuals of all ages, races, and ethnicities.
- Globally, the estimated number of persons living with epilepsy (PWE) is 50 million. India is home to about one-sixth of this population. In India, there are about 10–12 million epileptics living there.
- An individual may be diagnosed with epilepsy if they have an epilepsy syndrome or have experienced an unprovoked seizure and have a high probability (>60%) of experiencing another seizure within the next ten years.

## 8. Types of Epileptic Seiures

![image](https://github.com/aitijhyasarkar/SeizureSafeguard/assets/91305796/dedd39c7-4655-4420-8a0a-95efde674631)

## 9. Epilepsy recent trends and data

- EPILEPSY ACCOUNTS FOR A SIGNIFICANT PROPORTION OF THE WORLD’S DISEASE BURDEN, AFFECTING AROUND 50 MILLION PEOPLE WORLDWIDE.
- ABOUT 3 OUT OF 10 PEOPLE CONTINUE TO HAVE SEIZURES DESPITE TRYING OUT DIFFERENT TREATMENTS. 
- A FIRST “GRAND MAL” CONVULSION IS FRIGHTENING, YET PROSPECTIVE, POPULATION-BASED STUDIES INDICATE THAT WE ALL FACE AN 8-10% LIFETIME RISK OF ONE SEIZURE1 AND A 3% CHANCE OF EPILEPSY
![image](https://github.com/aitijhyasarkar/SeizureSafeguard/assets/91305796/8398edac-0658-4e39-8bb1-794a824e458b)

## 10. Need of EEG

- The EEG is used to evaluate several types of brain disorders. When epilepsy is present, seizure activity will appear as rapid spiking waves on the EEG.
- People with lesions of their brain, which can result from tumors or stroke, may have unusually slow EEG waves, depending on the size and the location of the lesion.
- The test can also be used to diagnose other disorders that influence brain activity, such as Alzheimer's disease, certain psychoses, and a sleep disorder called narcolepsy.
- The EEG may also be used to determine the overall electrical activity of the brain (for example, to evaluate trauma, drug intoxication, or extent of brain damage in comatose patients). The EEG may also be used to monitor blood flow in the brain during surgical procedures.

## 11. How EEG works in detecting epilepsy
 
- Hans Berger, a German psychiatrist, discovered the human electroencephalogram (EEG) in 1929. Since then, EEG has been a key tool in diagnosing and treating patients with seizure disorders. It helps determine seizure type, epilepsy syndrome, and aids in selecting appropriate antiepileptic medications. 
- An EEG is a test that detects abnormalities in brain waves, or in the electrical activity of the brain. During the procedure, electrodes consisting of small metal discs with thin wires are pasted onto your scalp. The electrodes detect tiny electrical charges that result from the activity of brain cells.
- The charges are amplified and appear as a graph on a computer screen, or as a recording that may be printed out on paper. A healthcare provider then interprets the reading.

## 12. Existing Devices

### 12.1 SEIZALARM
 Alerts emergency contacts when seizure-like motion or low/elevated heart rate is detected.
 \
✔️App includes a log dashboard where reports can be exported to share with doctor.
\
❌You must have an Apple Watch to effectively detect motion

### 12.2 EMBRACE 2
Utilises Electrodermal Activity to evaluate the ease with which an electrical signal travels through the skin. 
Fluctuations in the skin occur from alterations in the brain during a convulsive seizure. 
 \
✔️It also has applications such as an event detector and a dairy application
\
❌It does not detect complex partial seizures or absence seizures.

## 13. Our Differentiating Factor
There have been many seizure detection products over the years.
Many of them work by detecting abnormal movement. 
Many non-invasive options are geared towards night-time monitoring for parents of children with epilepsy.
\
\
We can offer a better accuracy owing to the fact that we will be tracking EEG data to detect epileptic seizure.


## 14. Future Scope of Our Project

- Integration with Electronic Health Records
- Customization and Personalization
- Telemedicine Integration
- Partnerships with Healthcare Institutions
- Continuous Research and Development


## 15. Conclusion

Our project represents a significant step forward in the field of healthcare technology, specifically in the realm of epilepsy detection and management. By harnessing the power of IoT technologies, we have developed an automated system that can detect seizures in individuals with epilepsy in real-time.
Through the utilization of wearable sensors and sophisticated algorithms, our system continuously monitors physiological signals and movement patterns, enabling timely detection of seizure activity. This functionality is crucial in providing prompt assistance and intervention, ultimately improving the safety and well-being of individuals living with epilepsy.
Furthermore, our project emphasizes user-friendliness and accessibility, with a focus on developing a seamless interface for both users and healthcare professionals. By prioritizing ease of use and comprehensive data analysis, we aim to enhance the quality of life for individuals with epilepsy and streamline the management process for caregivers and medical personnel.
Looking ahead, our project holds promise for scalability and integration with emerging technologies. We envision future collaborations with healthcare institutions to further refine and expand the capabilities of our system, ultimately advancing the standard of care for epilepsy patients worldwide.
In essence, our project represents more than just a technological innovation; it embodies our commitment to improving healthcare outcomes and making a meaningful difference in the lives of those affected by epilepsy.
