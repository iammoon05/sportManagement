import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import {MatTabsModule} from '@angular/material/tabs';
import { ProfileCard } from '../profile/profile.component';
import { ComponentPortal, Portal, PortalModule } from '@angular/cdk/portal';
import { CarouselModule } from 'primeng/carousel';
import { ButtonModule } from 'primeng/button';
import {MatCardModule} from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'my-options-carousel',
  templateUrl: 'myOptionsCarousel.component.html',
  standalone: true,
  imports: [MatTabsModule, ProfileCard, PortalModule, CarouselModule, ButtonModule, MatCardModule, MatIconModule],
})
export class MyOptionsCarousel implements AfterViewInit, OnInit{

  selectedTabPortal: Portal<any>;
  portalTab: Portal<any>;
  otherTab: Portal<any>;;
  staticTabs = [
    {
      header: "Profile",
      subHeader: "Manage your settings",
      icon: "account_circle",
      content: ProfileCard
    },
    {
      header: "Membership",
      subHeader: "See memberships",
      icon: "badge"
    },
    {
      header: "License and transfer",
      subHeader: "See and administer your licenses",
      icon: "assured_workload"
    },
    {
      header: "Roles",
      subHeader: "See your active roles",
      icon: "schema"
    },
    {
      header: "Competence",
      subHeader: "See your competences",
      icon: "military_tech"
    }
  ]

  public currentPage: number = 0;
  public numberOfPages: number = 0;
  public itemsInView: number = 3;
  public isNextDisabled: boolean = true;
  public isPrevDisabled: boolean = true;

  public responsiveOptions: any[] | undefined;



  ngAfterViewInit(): void {
    this.portalTab = new ComponentPortal(ProfileCard);
    this.selectedTabPortal = this.portalTab;
  }

  ngOnInit(): void {
    

    this.responsiveOptions = [
      {
          breakpoint: '50px',
          numVisible: 1,
          numScroll: 1
      },
      {
          breakpoint: '50px',
          numVisible: 2,
          numScroll: 1
      },
      {
          breakpoint: '50px',
          numVisible: 1,
          numScroll: 1
      }
    
    ];
  }


  changeSelectedTab(tabName: string) {
    console.log(tabName)
    if (tabName === 'Profile') {
      this.selectedTabPortal = this.portalTab;
    }
    if (tabName !== 'Profile') {
      console.log('tried changing')
      this.selectedTabPortal = new ComponentPortal(ComponentPortalExample);
    }
  }


}

@Component({
  selector: 'component-portal-example',
  template: 'Hello, this is a component portal',
  standalone: true,
})
export class ComponentPortalExample {}
