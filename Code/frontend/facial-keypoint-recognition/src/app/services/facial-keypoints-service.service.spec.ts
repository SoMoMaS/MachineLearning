import { TestBed } from '@angular/core/testing';

import { FacialKeypointsServiceService } from './facial-keypoints-service.service';

describe('FacialKeypointsServiceService', () => {
  let service: FacialKeypointsServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FacialKeypointsServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
