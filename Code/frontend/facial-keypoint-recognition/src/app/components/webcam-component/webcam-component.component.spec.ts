import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WebcamComponentComponent } from './webcam-component.component';

describe('WebcamComponentComponent', () => {
  let component: WebcamComponentComponent;
  let fixture: ComponentFixture<WebcamComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WebcamComponentComponent]
    });
    fixture = TestBed.createComponent(WebcamComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
