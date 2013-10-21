;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; HW7 blocks world + painting (stub)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain hw7)
  (:requirements :strips)
  (:predicates (Block ?obj)(Sprayer ?obj)(Color ?color)  (on-table ?obj) (arm-empty) (on-arm ?obj)(is-color ?color ?obj)
	)

  (:action pick-up 
      :parameters (?obj)
      :precondition (and (arm-empty) (on-table ?obj) (Sprayer ?obj))
      :effect (and (not (arm-empty)) (on-arm ?obj)))

  (:action put-down 
      :parameters (?obj)
      :precondition (and (not (arm-empty)) (on-arm ?obj))
      :effect (and (arm-empty) (not (on-arm ?obj)) ) )

  (:action spray-paint 
      :parameters (?block ?sprayer ?color)
      :precondition (and (Sprayer ?sprayer) (on-arm ?sprayer) (is-color ?color ?sprayer) (Block ?block) (Color ?color) ) 
      :effect   (is-color ?color ?block) )
 )
