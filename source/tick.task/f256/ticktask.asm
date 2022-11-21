; ************************************************************************************************
; ************************************************************************************************
;
;		Name:		ticktask.asm
;		Purpose:	Tick task handlere
;		Created:	21st November 2022
;		Reviewed: 	No.
;		Author : 	Paul Robson (paul@robsons.org.uk)
;
; ************************************************************************************************
; ************************************************************************************************

		.section 	code

; ************************************************************************************************
;
;							Tick Handler - sort of interrupt routine
;
; ************************************************************************************************

		.send 		code

TickHandler:
;		lda 	#33
;		jsr 	EXTPrintCharacter	
		rts

		.section 	storage
LastTick:
		.fill 		1
		.send 		storage

; ************************************************************************************************
;
;									Changes and Updates
;
; ************************************************************************************************
;
;		Date			Notes
;		==== 			=====
;
; ************************************************************************************************
