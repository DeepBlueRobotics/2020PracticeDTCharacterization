package dc;

import edu.wpi.first.wpilibj.DoubleSolenoid;

public class GearShift {

	private static DoubleSolenoid gearShift = new DoubleSolenoid(6,7);

	public static void shift() {
		boolean isHigh = true;
		if(isHigh) {
			gearShift.set(DoubleSolenoid.Value.kForward);
		} else {
			gearShift.set(DoubleSolenoid.Value.kReverse);
		}
	}

}