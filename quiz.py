# quiz game

# imports
from random import shuffle
from question import MyQuestion


def run_game(frame):
    # function to create all game elements
    q1 = MyQuestion(frame,
                    'What is the moment of inertia, I for a disc?',
                    'I = MR^2',
                    'I = 1/12 *  ML^2',
                    'I = 1/2 *  MR^2',
                    'I = 1/2 *  Mk^2',
                    'This is the Moment of Inertia for a particle.',
                    'This is the Moment of Inertia for a stick.',
                    'This is the Moment of Inertia for a disc.',
                    'This Moment of Inertia is for a particle of a disc and involves k, \nwhich is the radius of gyration.',
                    3
                    )

    q2 = MyQuestion(frame,
                    'What is the Rotational Kinetic Energy of a rolling disc?',
                    '0.5 * mv^2',
                    '0.25 * mr^2w^2',
                    '0.5 * mr^2',
                    '0.25 * Iw^2',
                    'This is a formula for Linear Kinetic Energy.',
                    'For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2 = 0.5 * (0.5 * mr^2)w^2 = 0.25 * mr^2w^2 ',
                    'This is the Moment of Inertia of a disc. \nNote: This formula does not involve any kind of velocity. \nThus, it cannot be Kinetic Energy.',
                    'For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2. \n\nWhen the Moment of Inertia of the disc is substituted, \nthen only the 0.25 appear.',
                    2
                    )

    q3 = MyQuestion(frame,
                    'What is the angular momentum, L for an orbiting particle?',
                    'L = mr^2w',
                    'L = mv',
                    'L = wr',
                    'L = mr^2',
                    'The angular momentum for an orbiting paticle is given as, \nL = Iw. \n\nThus, when the Moment of Inertia(I) of a disc is substituted, \nL = mr^2w ',
                    'Recall that LINEAR Momentum is the product of mass and velocity. \np = mv',
                    'This formula is used to find linear velocity. \nv = wr',
                    'This formula is the Moment of Inertia for a particle. \nI = mr^2',
                    1
                    )

    q4 = MyQuestion(frame,
                    'Rate of change of angular momentum is equal to ___________?',
                    'torque',
                    'force',
                    'moment of inertia',
                    'angular velocity',
                    'Torque is the rate of change of angular momentum.',
                    'Force is the rate of change of LINEAR momentum.',
                    'Moment of Inertia is the product of mass and square of distance.',
                    'Angular Velocity is the rate of change of Angular Displacement in radians per second.',
                    1
                    )

    q5 = MyQuestion(frame,
                    'What is the unit for Angular Momentum?',
                    'kgms^-1',
                    'kgm^2(s^-2)',
                    'kgm^2(s^-1)',
                    'kgm^2',
                    'This unit is for LINEAR Momentum. \nLinear and Angular Momentum have different units due to involving different quantities. \np = mv = kgms^-1',
                    'This unit is for Torque. \nTorque is the product of Moment of Inertia and Angular Acceleration. \nT = Ia = kgm^2(s^-2)',
                    'This is the unit for Angular Momentum. \nL = Iw = (MR^2)w = (kgm^2)s^-1',
                    'This is the unit for Moment of Inertia. \nI = mr^2 = kgm^2',
                    3
                    )

    q6 = MyQuestion(frame,
                    'What real force keeps a satellite in a circular orbit around the earth?',
                    'Thrust',
                    'Gravity',
                    'Centripetal force',
                    'There is no force in space',
                    'This is a propulsive force. ',
                    'Gravitational pull of earth acts on the satellite which keeps the satellite in a circular orbit \naround the earth provided its velocity balances the gravitational force.',
                    'Centripetal force is just a net force.',
                    'Gravitational force exists in space.',
                    2
                    )

    q7 = MyQuestion(frame,
                    'The velocity is always __________ to the line of a circle.',
                    'tangent',
                    'towards the center',
                    'outwards',
                    'inwards',
                    'Velocity acts tangent to a circle.',
                    'Centripetal force acts towards the center of a circle.',
                    'Invalid answer.',
                    'Invalid answer.',
                    1
                    )

    q8 = MyQuestion(frame,
                    'What is the force that keeps an object in circular motion?',
                    'Centrifugal force',
                    'Centripetal force',
                    'Center-fleeing force',
                    'Gravitational Force',
                    'Centrifugal force is the tendency of an object to \nfly away from the center of a curved path.',
                    'Centripetal force is the net force keeping an object in circular motion. \nThe resultant force of all real forces acting on the object, \nthat acts towards the centre of the circular path is responsible for its circular motion.',
                    'This force is also called Centrifugal Force which is \nthe tendency of an object to fly away from the center of a curved path.',
                    'This is an attractive force which occurs between \nmasses of objects and it is not a net force.',
                    2
                    )

    # shuffling questions
    qlist = [q1, q2, q3, q4, q5, q6, q7, q8]
    shuffle(qlist)

    for question in qlist:
        question.pf.tkraise()
