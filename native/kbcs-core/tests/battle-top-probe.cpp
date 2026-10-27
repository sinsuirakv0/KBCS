// 描画専用fixture。解決済みの表示値を同じ所有構造へ入れ、更新/生成は検証対象外。
#include "../src/actor.cpp"
extern "C" __declspec(dllexport) uint32_t top_probe(const int *input,const KbcsRenderCut *cuts,int count,const KbcsRenderCut *fever,int fever_count,KbcsDrawCommand *out,int *written){
 KbcsBattleConfig c{};c.screen.viewport_width=input[0];c.rules.score_type=input[1];c.rules.time_limit=input[2];c.rules.point.fever_count=input[8]?3:0;c.rules.point.fever[2]=300;
 KbcsBattle b(c);b.result={input[3],0,0,input[4],0,0};b.score_display={0,0,0,input[4],input[5]};b.points.score=input[4];b.points.gauge=input[6];b.points.wait=input[7];b.points.frame=input[9];
 return kbcs_core_battle_top_draw(&b,cuts,count,fever,fever_count,nullptr,out,64,written);
}
