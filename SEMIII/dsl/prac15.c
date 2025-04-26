#include<stdio.h>
#include <string.h>
# define MAX 100
char stack[MAX];
int top=-1;
void push(char stack[MAX],char opt);
char pop(char stack[MAX]);
void InfixToPostfix(char infix[],char postfix[]);
int getPriority(char opt);

int main(){
char infix[MAX];
char postfix[MAX];
printf("Enter a infix expression:");
gets(infix);
strcpy(postfix,"");
printf("postfix expression is:");
InfixToPostfix(infix,postfix);
puts(postfix);
return 0;
}
void InfixToPostfix(char infix[],char postfix[]){
    int i=0,j=0;
    char temp;
while(infix[i]!='\0'){
    if(infix[i]=='('){
        push(stack,infix[i]);
        i++;
    }
    else if(infix[i]==')'){
           while(top!=-1 && stack[top]!='(') {
                postfix[j]=pop(stack);
                j++;
            }
            if(top==-1){
                printf("invalid");
            }
            pop(stack);
            i++;
            }
     else if(isdigit(infix[i])|| isalpha(infix[i])){
        postfix[j]=infix[i];
        j++;
        i++;
     }
     else if(infix[i]=='+' || infix[i]=='-'|| infix[i]=='*' || infix[i]=='%' || infix[i]=='/'){
        while((top!=-1)&&(stack[top]!='(')&&(getPriority(stack[top])>=getPriority(infix[i]))){
                postfix[j]=pop(stack);
                j++;
              }
              push(stack,infix[i]);
              i++;
     }else{
     printf("invalid");
     }

}
while(top!=-1 && stack[top]!='('){
        postfix[j]=pop(stack);
        j++;
      }
      postfix[j]='\0';

}

void push(char stack[],char opt){
  if(top==MAX-1){
    printf("stack overflow");
  }else{
  top++;
  stack[top]=opt;
  }
}

char pop(char stack[]){
    char val;
if(top==-1){
    printf("underflow");
}else{
val=stack[top];
top--;
}
return val;
}

int getPriority(char opt){
    if(opt=='*'||opt=='%'||opt=='/'){
        return 1;
    }else if(opt=='+'||opt=='-'){
        return 0;
    }

}




