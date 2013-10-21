;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; HW7 blocks world + painting (stub)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain hw7)
  (:requirements :strips)
  (:predicates 
	(Block ?obj)
	(Sprayer ?obj)
	(Color ?obj)
	(arm-empty)
	(on-arm ?obj)
	(is-color ?obj ?obj)
	)

  (:action pick-up 
	:parameters (?a)
        :precondition (and (arm-empty) (Sprayer ?a))
        :effect (and (not (arm-empty)) (on-arm ?a)))

  (:action put-down 
	:parameters (?a)
        :precondition (and (not (arm-empty)) (Sprayer ?a) (on-arm ?a))
        :effect (and (arm-empty) (not (on-arm ?a)) ) )

  )
