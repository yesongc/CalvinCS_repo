/*Yesong Choi
  yc38
  Feb 16, 2017
*/

#include <stdio.h>   
#include <signal.h>  //signal handler, alarm
#include <stdbool.h> //true false
#include <string.h>  //strcmp
#include <unistd.h>  
#include <stdlib.h>  //atoi

/*global variables for interrupt and message*/
bool interrupt = false; /*Value for -i, +i*/
char *message = "HIHIHIHIHIHIIHIHHIHI\n";

/*alarmhandler function prints out an annoying message when the signal function receives SIGALRM set off by the alarm function
* parameters: 
* returns an annoying message.
*/
void alarmhandler (int sig);
void alarmhandler (int sig){
	printf("%s\n", message);
}

/*interrupt handler function prints out an appropriate message when SIGINT is received by the signal function.
* parameters:
* returns an annoying message.
*/
void interrupthandler (int sig){
	printf("\n sorry, you can't exit..\n");
}

/*main function checks to see if there are any arguments given by the user and acts accordingly.
* parameters: argc (argument counter) and *argv[] (argument vector)
* returns an annoying message.
*/
int main (int argc, char *argv[]){
	int p;
	int timer = 5;	/*Value for +t*/

	for (p = 1; p < argc; p++){
		/*if there is a -i, then disable interrupts*/
		if (strcmp(argv[p], "-i") == 0) {
			interrupt = false;
			
		}
		/*if there is a +i, enable interrupts*/
		else if (strcmp(argv[p], "+i")==0) {
			interrupt = true;
			
		}
		/*if there is a +t, enable timer*/
		else if (strcmp(argv[p], "+t")==0) {
			timer = atoi(argv[p+1]);
			
		}
		/*if there is a -m, enable message, and set user input as new message*/
		else if (strcmp(argv[p], "-m")==0) {
			message = argv[p+1];
			
		}
	}
	/*if you receive SIGALRM, then go to signalhandler function*/
	signal(SIGALRM, alarmhandler);
	/*if interrupt is off, then go to the interrupt handler function when receiving a SIGINT*/	
	if (interrupt == false) {
		signal(SIGINT, interrupthandler);
	}
	/*infinite loop that sets an alarm that gives off SIGALRM every "timer" seconds, and also pauses the program until it receives
	a SIGALRM*/
	while(true){
		alarm(timer);
		pause();

	}
				
}

