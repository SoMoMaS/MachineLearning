import { TestBed } from '@angular/core/testing';

import { ImageModificationService } from './image-modification.service';

describe('ImageModificationService', () => {
  let service: ImageModificationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ImageModificationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
