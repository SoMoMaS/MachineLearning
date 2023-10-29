import { Position } from './position'

export interface FacialKeypoints {
    left_eye_center: Position;
    right_eye_center: Position;
    left_eye_inner_corner: Position;
    left_eye_outer_corner: Position;
    right_eye_inner_corner: Position;
    right_eye_outer_corner: Position;
    left_eyebrow_inner_end: Position;
    left_eyebrow_outer_end: Position;
    right_eyebrow_inner_end: Position;
    right_eyebrow_outer_end: Position;
    nose_tip: Position;
    mouth_left_corner: Position;
    mouth_right_corner: Position;
    mouth_center_top_lip: Position;
    mouth_center_bottom_lip: Position;
}
