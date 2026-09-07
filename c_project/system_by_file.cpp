#include <stdio.h>
#include <string.h>

struct patient
{
    int id;
    char name[50];
    int age;
    char gender[10];
    char disease[20];
};

int main()
{
    int option, pass;
    int newId;
    int found;
    char user[20];

    struct patient p;
    struct patient temp;

    FILE *fp;

    printf("Enter your username: ");
    scanf("%s", user);

    printf("Enter your password: ");
    scanf("%d", &pass);

    if(strcmp(user, "Admin") == 0 && pass == 1234)
    {
        printf("\nWELCOME TO PATIENT MANAGEMENT SYSTEM\n");
        printf("---------------------------------------\n");

        do
        {
            printf("\n\nWhat do you want to do:\n");
            printf("1] ADD PATIENT\n");
            printf("2] VIEW PATIENTS\n");
            printf("3] SEARCH PATIENT\n");
            printf("4] EXIT\n");

            printf("\nEnter your option: ");
            scanf("%d", &option);

            switch(option)
            {
                
                case 1:

                    printf("\nEnter patient ID: ");
                    scanf("%d", &newId);

                    found = 0;

                    
                    fp = fopen("patients.txt", "r");

                    if(fp != NULL)
                    {
                        while(fscanf(fp, "%d %s %d %s %s",
                                     &temp.id,
                                     temp.name,
                                     &temp.age,
                                     temp.gender,
                                     temp.disease) == 5)
                        {
                            if(temp.id == newId)
                            {
                                found = 1;
                                break;
                            }
                        }

                        fclose(fp);
                    }

                    if(found == 1)
                    {
                        printf("\nPatient ID already exists!");
                        break;
                    }

                    
                    p.id = newId;

                    printf("Enter patient name: ");
                    scanf("%s", p.name);

                    printf("Enter age: ");
                    scanf("%d", &p.age);

                    printf("Enter gender: ");
                    scanf("%s", p.gender);

                    printf("Enter disease: ");
                    scanf("%s", p.disease);

                   
                    fp = fopen("patients.txt", "a");

                    if(fp == NULL)
                    {
                        printf("\nFile cannot be opened!");
                        break;
                    }

                   
                    fprintf(fp, "%d %s %d %s %s\n",
                            p.id,
                            p.name,
                            p.age,
                            p.gender,
                            p.disease);

                    fclose(fp);

                    printf("\nPatient added successfully!");

                    break;
                    
                case 2:
                    fp = fopen("patients.txt", "r");
                    if(fp == NULL)
                    {
                        printf("\nNo patient records found!");
                        break;
                    }
                    printf("\n\n========== PATIENT RECORDS ==========\n");

                    while(fscanf(fp, "%d %s %d %s %s",
                                 &p.id,
                                 p.name,
                                 &p.age,
                                 p.gender,
                                 p.disease) == 5)
                    {
                        printf("\nID      : %d", p.id);
                        printf("\nName    : %s", p.name);
                        printf("\nAge     : %d", p.age);
                        printf("\nGender  : %s", p.gender);
                        printf("\nDisease : %s", p.disease);
                        printf("\n-------------------------------------");
                    }

                    fclose(fp);

                    break;
                    
                case 3:
                    printf("\nEnter Patient ID to search: ");
                    scanf("%d", &newId);

                    found = 0;
                    fp = fopen("patients.txt", "r");
                    if(fp == NULL)
                    {
                        printf("\nNo patient records found!");
                        break;
                    }

                    while(fscanf(fp, "%d %s %d %s %s",
                                 &p.id,
                                 p.name,
                                 &p.age,
                                 p.gender,
                                 p.disease) == 5)
                    {
                        if(p.id == newId)
                        {
                            printf("\n\n========== PATIENT FOUND ==========\n");

                            printf("ID      : %d\n", p.id);
                            printf("Name    : %s\n", p.name);
                            printf("Age     : %d\n", p.age);
                            printf("Gender  : %s\n", p.gender);
                            printf("Disease : %s\n", p.disease);

                            found = 1;
                            break;
                        }
                    }

                    fclose(fp);

                    if(found == 0)
                    {
                        printf("\nPatient not found!");
                    }
                    break;
                case 4:
                    printf("\nThank you for using Patient Management System!\n");
                    break;
                default:

                    printf("\nInvalid option!");
            }

        } while(option != 4);
    }
    else
    {
        printf("\nEnter valid credentials!");
    }

    return 0;
}
