

(define (domain hw7)
  (:requirements :strips)
  (:predicates (Block ?obj)(Sprayer ?obj)(Color ?color)  (on-table ?obj) (arm-empty) (on-arm ?obj)(is-color ?color ?obj) (Can ?can) (Brush ?brush) (clean ?brush) (Bucket ?bucket) (clear ?obj) (on ?obj1 ?obj2)  (has-color ?color ?obj)
	)

  (:action pick-up 
      :parameters (?obj)
      :precondition (and (arm-empty) (on-table ?obj) (clear ?obj) )
      :effect (and (not (arm-empty)) (on-arm ?obj) (not(on-table ?obj)) (not(clear ?obj)) ))

  (:action put-down 
      :parameters (?obj)
      :precondition (on-arm ?obj)
      :effect (and (arm-empty) (not (on-arm ?obj)) (clear ?obj) (on-table ?obj) ))

  (:action spray-paint 
      :parameters (?obj ?sprayer ?color)
      :precondition (and (Sprayer ?sprayer) (on-arm ?sprayer) (has-color ?color ?sprayer) (Color ?color) (on-table ?obj) ) 
      :effect   (is-color ?color ?obj) )

  (:action load-brush 
      :parameters (?brush ?can ?color)
      :precondition (and (Brush ?brush) (Can ?can) (Color ?color) (clean ?brush) (on-arm ?brush) (clear ?can) (has-color ?color ?can))
      :effect (and (not (clean ?brush)) (has-color ?color ?brush) ) )

  (:action brush-paint 
      :parameters (?obj ?color ?brush)
      :precondition (and (Color ?color) (Brush ?brush) (on-arm ?brush)
                    (has-color ?color ?brush) (clear ?obj) (on-table ?obj))
      :effect (is-color ?color ?obj) )

  (:action wash-brush 
      :parameters (?brush ?color ?bucket)
      :precondition (and (Brush ?brush) (Color ?color) (Bucket ?bucket) (on-arm ?brush) (clear ?bucket) (has-color ?color ?brush) )
      :effect (and (not (has-color ?color ?brush)) (clean ?brush) ))

  (:action unstack 
      :parameters (?obj1 ?obj2)
      :precondition (and (arm-empty) (on ?obj1 ?obj2) (clear ?obj1))
      :effect (and (not (arm-empty)) (not (on ?obj1 ?obj2)) (not(clear ?obj1)) (on-arm ?obj1) (clear ?obj2 )))

  (:action stack 
      :parameters (?obj1 ?obj2)
      :precondition (and (on-arm ?obj1) (clear ?obj2))
      :effect (and (arm-empty) (on ?obj1 ?obj2) (clear ?obj1) (not(clear ?obj2)) (not(on-arm ?obj1))  ))



 )
