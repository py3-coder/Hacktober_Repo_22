const HEADPOSTURE_ROTATION_X_L_THRESHOLD = 0.3;
const HEADPOSTURE_ROTATION_X_S_THRESHOLD = 0.0;
const HEADPOSTURE_ROTATION_Y_THRESHOLD = 0.3;
const HEADPOSTURE_ROTATION_Z_THRESHOLD = 0.3;
const SCREEN_DISTANCE_POSTION_THRESHOLD = 0.3;

/**
 * 
 * @param {Array} rotation 
 */
function isHeadPostureOK(rotation) {
	return [
		rotation[0] < HEADPOSTURE_ROTATION_X_L_THRESHOLD && rotation[0] > HEADPOSTURE_ROTATION_X_S_THRESHOLD,
		Math.abs(rotation[1]) < HEADPOSTURE_ROTATION_Y_THRESHOLD,
		Math.abs(rotation[2]) < HEADPOSTURE_ROTATION_Z_THRESHOLD
	];
}

/**
 * 
 * @param {float} positionZ 
 */
function isScreenDistanceOK(positionZ) {
	return positionZ < SCREEN_DISTANCE_POSTION_THRESHOLD;
}
