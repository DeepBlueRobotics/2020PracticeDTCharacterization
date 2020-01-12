package frc.robot;

import edu.wpi.first.wpilibj.DoubleSolenoid;

public class GearShift {

	private static DoubleSolonoid gearShift = new DoubleSolonoid(6,7);

	public static void shift() {
		boolean isHigh = true;
		if(isHigh) {
			shift.set(DoubleSolenoid.Value.kForward);
		} else {
			shift.set(DoubleSolenoid.Value.kReverse);
		}
	}

}