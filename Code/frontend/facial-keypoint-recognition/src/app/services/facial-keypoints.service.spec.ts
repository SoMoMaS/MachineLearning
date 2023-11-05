import { TestBed } from '@angular/core/testing';

import { FacialKeypointsService } from './facial-keypoints.service';

describe('FacialKeypointsService', () => {
  let service: FacialKeypointsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FacialKeypointsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
