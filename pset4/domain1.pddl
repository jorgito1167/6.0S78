

(define (domain hw7)
  (:requirements :strips)
  (:predicates (Block ?obj)(Sprayer ?obj)(Color ?color)  (on-table ?obj) (arm-empty) (on-arm ?obj)(is-color ?color ?obj) (Can ?can) (Brush ?brush) (Clean ?brush)
	)

  (:action pick-up 
      :parameters (?obj)
      :precondition (and (arm-empty) (on-table ?obj))
      :effect (and (not (arm-empty)) (on-arm ?obj)))

  (:action put-down 
      :parameters (?obj)
      :precondition (and (not (arm-empty)) (on-arm ?obj))
      :effect (and (arm-empty) (not (on-arm ?obj)) ) )

  (:action spray-paint 
      :parameters (?block ?sprayer ?color)
      :precondition (and (Sprayer ?sprayer) (on-arm ?sprayer) (is-color ?color ?sprayer) (Block ?block) (Color ?color) ) 
      :effect   (is-color ?color ?block) )

  (:action load-brush 
      :parameters (?brush ?can ?color)
      :precondition (and (Brush ?brush) (Can ?can) (Color ?color) (Clean ?brush) (on-arm ?brush) (is-color ?color ?can))
      :effect (and (not (Clean ?brush)) (is-color ?color ?brush) ) )

  (:action brush-paint 
      :parameters (?block ?color ?brush)
      :precondition (and (Block ?block) (Color ?color) (Brush ?brush) (on-arm ?brush)
                    (is-color ?color ?brush))
      :effect (is-color ?color ?block) )



 )
