// 終了演出の時計。オンライン・広告・課金コンティニューの状態を含めない。
extern "C" uint32_t kbcs_core_battle_popup_step(int32_t release,KbcsBattlePopup *state){
 if(!state||release<0||release>1||state->phase<0||state->phase>3||state->scale_frame<0||state->scale_frame>4)return 1;
 auto &s=*state;
 // 008865b8 / 005f72cc: type0はタップ解放でSE11→close、5表示更新後に次の報酬へ。
 if(s.phase==0){if(s.scale_frame>3)s.phase=1;else ++s.scale_frame;}
 else if(s.phase==1){++s.flash;if(release){s.phase=2;s.wait=0;}}
 else if(s.phase==2&&++s.wait>=5){s.phase=3;s.wait=0;}
 return 0;
}
extern "C" uint32_t kbcs_core_battle_popup_layout(const KbcsBattlePopupInput *input,KbcsBattlePopupLayout *out){
 if(!input||!out||input->viewport<960||input->viewport>3840||input->count<1||input->count>8||input->scale_frame<0||input->scale_frame>4)return 1;
 const auto &in=*input;KbcsBattlePopupLayout value{};int width=0;
 for(int i=0;i<in.count;++i){if(in.widths[i]<0||in.widths[i]>100000)return 1;width=std::min(800,std::max(width,in.widths[i]));}
 const int height=in.count<3?((in.count^3)*-18+180):in.count*36+72;
 width=std::max(670,width+54);const int x=in.viewport/2-width/2,y=401;
 static constexpr int scales[]={0,50,80,90,100};const int scale=scales[in.scale_frame];
 // 00885170の幅/高さ/座標、00886a84の拡大率、0044626cの9領域をそのまま返す。
 const int bx=x+width/2-(width/2*scale)/100,by=y+height/2-(height/2*scale)/100,bw=width*scale/100,bh=height*scale/100;
 value.body[0]=bx;value.body[1]=by;value.body[2]=bw;value.body[3]=bh;value.text_y=y+height/2-(in.count-1)*18;
 for(int i=0;i<in.count;++i){value.text_scale[i]=in.widths[i]>800?800.f/float(in.widths[i]):1.f;value.text_x[i]=in.viewport/2-std::min(800,in.widths[i])/2;}
 const int px=in.padding[0],py=in.padding[1];if(px<0||py<0||px*2>in.cut[2]||py*2>in.cut[3])return 1;
 const int dx[]={bx,int(float(bx)+2.7f*float(px)),int(float(bx+bw)-2.7f*float(px))};
 const int dy[]={by,int(float(by)+2.7f*float(py)),int(float(by+bh)-2.7f*float(py))};
 const int dw[]={int(2.7f*float(px)),int(float(bw)-2.7f*float(px*2)),int(2.7f*float(px))};
 const int dh[]={int(2.7f*float(py)),int(float(bh)-2.7f*float(py*2)),int(2.7f*float(py))};
 const int sx[]={in.cut[0],in.cut[0]+px,in.cut[0]+in.cut[2]-px},sy[]={in.cut[1],in.cut[1]+py,in.cut[1]+in.cut[3]-py};
 const int sw[]={px,in.cut[2]-px*2,px},sh[]={py,in.cut[3]-py*2,py};
 for(int r=0;r<3;++r)for(int c=0;c<3;++c){int *p=value.parts[r*3+c];p[0]=dx[c];p[1]=dy[r];p[2]=dw[c];p[3]=dh[r];p[4]=sx[c];p[5]=sy[r];p[6]=sw[c];p[7]=sh[r];}
 *out=value;return 0;
}
extern "C" uint32_t kbcs_core_battle_ending_step(int32_t mode,int32_t point,KbcsBattleEnding *state){
 if(!state||(mode!=1&&mode!=2&&mode!=4&&mode!=7))return 1;
  auto &e=*state;const int old=e.frame;e.frame=int32_t(uint32_t(e.frame)+1);
  if(e.guard&&++e.guard>5){e.guard=0;e.action=302;}
  // 005e1a5c / 005eb040 / 005edb40 / 005ef020。時計は表示更新単位。
  if(!e.phase){if(e.frame>19){e.phase=1;e.frame=0;}return 0;}
  if(mode==2){if(e.phase==1&&e.frame>43){e.phase=2;e.frame=0;}else if(e.phase==2&&old>=79){e.phase=4;e.frame=0;}return 0;}
  if(e.phase<3){if(mode==1&&point&&e.phase==2&&old<=-2&&e.frame+100>45)e.frame=0;else if(old>=12){++e.phase;e.frame=(mode==1&&point&&e.phase==2)?-100:0;}return 0;}
  if(e.phase==3){if(mode==4){e.panel=std::min(96,e.panel+20);if(e.panel==96)e.phase=7;}else if(e.frame>=30){e.phase=6;e.frame=0;}}
  else if(e.phase==6){const int previous=e.panel;e.panel+=20;if(previous>61){e.panel=82;e.phase=7;}}
 return 0;
}
extern "C" uint32_t kbcs_core_battle_end_camera_step(KbcsBattleEndCamera *state){
 if(!state||state->width<2800||state->rows<1||state->rows>2||state->zoom<100||state->zoom>10000||state->moving<0||state->moving>2)return 1;
 auto &s=*state;
 // 005cb0e0: battle_zoom_castle_y=20、段別アンカー520/505、二段補正-51。
 const int cap=s.rows==2?8803:10000;
 if(!s.moving){s.zoom=std::min(cap,s.zoom+800);return 0;}
 if(s.moving==2){if(s.left<82&&s.zoom>=cap){s.left=0;s.moving=0;}else s.left-=s.left/2;}
 else{
  const float scale=float(s.zoom/100)/100.f;const int target=int((scale*float(s.width)-9600.f)/scale),delta=target-s.left;
  if(delta<82&&s.zoom>=cap){s.left=s.width-9600;s.moving=0;}
  else s.left+=delta/2;
 }
 s.zoom=std::min(cap,s.zoom+800);return 0;
}
extern "C" uint32_t kbcs_core_battle_music_cross(const KbcsBattleRewardRules *rules,int32_t previous,int32_t current,int32_t maximum,KbcsBattleMusic *state){
 if(!rules||!state||previous<0||current<0||maximum<0)return 1;
 const int rate=rules->music_threshold;if(rate<1||rate>99)return 0;
 const int threshold=int32_t(uint32_t(rate)*uint32_t(maximum))/100;
 if(threshold<previous&&current<=threshold){state->changed=1;state->started=1;state->delay=0;state->wait=45;state->id=-1;++state->serial;}
 return 0;
}
extern "C" uint32_t kbcs_core_battle_music_tick(const KbcsBattleRewardRules *rules,KbcsBattleMusic *state){
 if(!rules||!state||state->wait<0)return 1;
 if(state->wait>0&&!--state->wait){state->id=rules->music[0]!=rules->music[1]?rules->music[1]:-1;++state->serial;}
 return 0;
}
