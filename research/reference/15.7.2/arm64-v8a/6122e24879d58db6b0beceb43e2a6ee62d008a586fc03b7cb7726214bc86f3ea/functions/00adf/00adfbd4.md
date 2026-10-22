# 00adfbd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adfbd4.md)

## 関数情報

~~~json
{
  "address": "00adfbd4",
  "name": "_INIT_268",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10da53c93ca02b823ff4f11c1e8c798369f5ae9f444e086dd0f3e23b80a2d6d0",
  "source_text_sha256": "10da53c93ca02b823ff4f11c1e8c798369f5ae9f444e086dd0f3e23b80a2d6d0"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00418cb8](../00418/00418cb8.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"CgkIjM3y_ZQaEAIQAg"
"CgkIjM3y_ZQaEAIQAw"
"CgkIjM3y_ZQaEAIQBA"
"CgkIjM3y_ZQaEAIQBQ"
"CgkIjM3y_ZQaEAIQBg"
"CgkIjM3y_ZQaEAIQBw"
"CgkIjM3y_ZQaEAIQCA"
~~~
## 疑似コード 1/1 / UTF-8 9054 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_268(void)

{
  long lVar1;
  undefined4 local_118 [2];
  byte local_110;
  char local_10f [8];
  undefined7 uStack_107;
  char cStack_100;
  undefined2 uStack_ff;
  undefined1 uStack_fd;
  undefined4 uStack_fc;
  undefined4 local_f8 [2];
  byte local_f0;
  char local_ef [8];
  undefined7 uStack_e7;
  char cStack_e0;
  undefined2 uStack_df;
  undefined1 uStack_dd;
  undefined4 uStack_dc;
  undefined4 local_d8 [2];
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined2 uStack_bf;
  undefined1 uStack_bd;
  undefined4 uStack_bc;
  undefined4 local_b8 [2];
  byte local_b0;
  char local_af [8];
  undefined7 uStack_a7;
  char cStack_a0;
  undefined2 uStack_9f;
  undefined1 uStack_9d;
  undefined4 uStack_9c;
  undefined4 local_98 [2];
  byte local_90;
  char local_8f [8];
  undefined7 uStack_87;
  char cStack_80;
  undefined2 uStack_7f;
  undefined1 uStack_7d;
  undefined4 uStack_7c;
  undefined4 local_78 [2];
  byte local_70;
  char local_6f [8];
  undefined7 uStack_67;
  char cStack_60;
  undefined2 uStack_5f;
  undefined1 uStack_5d;
  undefined4 uStack_5c;
  undefined4 local_58 [2];
  byte local_50;
  char local_4f [8];
  undefined7 uStack_47;
  char cStack_40;
  undefined2 uStack_3f;
  undefined1 uStack_3d;
  undefined4 uStack_3c;
  long local_38;
  
                    /* catch() { ... } // from try @ 00adf1e4 with catch @ 00adfbe0
                       catch() { ... } // from try @ 00adf2f4 with catch @ 00adfbe0
                       catch() { ... } // from try @ 00adf3f0 with catch @ 00adfbe0
                       try { // try from 00adfbe0 to 00bdfcdf has its CatchHandler @ 00adec0c */
                    /* catch() { ... } // from try @ 00adfb8c with catch @ 00adfbe4 */
                    /* catch() { ... } // from try @ 00adf030 with catch @ 00adfbe8 */
  lVar1 = tpidr_el0;
                    /* catch() { ... } // from try @ 00adf02c with catch @ 00adfbec */
                    /* catch() { ... } // from try @ 00adefdc with catch @ 00adfbf0 */
                    /* catch() { ... } // from try @ 00adef1c with catch @ 00adfbf4 */
  local_38 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00adef58 with catch @ 00adfbf8
                       catch() { ... } // from try @ 00adf238 with catch @ 00adfbf8 */
                    /* catch() { ... } // from try @ 00adfb54 with catch @ 00adfbfc
                       catch() { ... } // from try @ 00adfbc0 with catch @ 00adfbfc */
                    /* catch() { ... } // from try @ 00adfb38 with catch @ 00adfc00
                       catch() { ... } // from try @ 00adfb70 with catch @ 00adfc00
                       catch() { ... } // from try @ 00adfba8 with catch @ 00adfc00 */
                    /* catch() { ... } // from try @ 00adf0c8 with catch @ 00adfc04 */
                    /* catch() { ... } // from try @ 00adf5bc with catch @ 00adfc08 */
                    /* catch() { ... } // from try @ 00adfab4 with catch @ 00adfc0c
                       catch() { ... } // from try @ 00adfaec with catch @ 00adfc0c */
                    /* catch() { ... } // from try @ 00adee1c with catch @ 00adfc10 */
                    /* catch() { ... } // from try @ 00adec80 with catch @ 00adfc14
                       catch() { ... } // from try @ 00adfa98 with catch @ 00adfc14 */
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a72e4._0_8_;
                    /* catch() { ... } // from try @ 00adfa80 with catch @ 00adfc30
                       catch() { ... } // from try @ 00adfad0 with catch @ 00adfc30
                       catch() { ... } // from try @ 00adfb20 with catch @ 00adfc30 */
                    /* catch() { ... } // from try @ 00aded74 with catch @ 00adfc34 */
                    /* catch() { ... } // from try @ 00adfa4c with catch @ 00adfc38 */
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_,7);
                    /* catch() { ... } // from try @ 00adfa30 with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfa68 with catch @ 00adfc44 */
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a72f7._0_8_;
                    /* catch() { ... } // from try @ 00adf9fc with catch @ 00adfc58 */
  uStack_bf = 0x6742;
                    /* catch() { ... } // from try @ 00adf85c with catch @ 00adfc5c */
                    /* catch() { ... } // from try @ 00adf80c with catch @ 00adfc60
                       catch() { ... } // from try @ 00adf894 with catch @ 00adfc60 */
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a80da._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002936ae._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._0_8_;
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_00291877._0_8_;
  local_110 = 0x24;
  local_f0 = 0x24;
  local_d0 = 0x24;
                    /* try { // try from 00adfce0 to 00bdfd77 has its CatchHandler @ 00adfce0
                       catch() { ... } // from try @ 00adfce0 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adfd88 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adff44 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0334 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0410 with catch @ 00adfce0 */
  local_b0 = 0x24;
  local_90 = 0x24;
  local_70 = 0x24;
  local_50 = 0x24;
  local_118[0] = 0;
  uStack_fd = 0;
  uStack_dd = 0;
  uStack_bd = 0;
  uStack_9d = 0;
  uStack_7d = 0;
  uStack_5d = 0;
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_00294526._0_8_;
  uStack_3d = 0;
  DAT_0109ff40 = 0;
  DAT_0109ff38 = 0;
  DAT_0109ff30 = &DAT_0109ff38;
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_118,local_118);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_b8,local_b8);
                    /* try { // try from 00adfd78 to 00bdfd87 has its CatchHandler @ 00ae081c */
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_98,local_98);
                    /* try { // try from 00adfd88 to 00bdfe5f has its CatchHandler @ 00adfce0 */
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_78,local_78);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_58,local_58);
  if ((local_50 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
  if ((local_90 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  if ((local_b0 & 1) != 0) {
                    /* try { // try from 00adfe60 to 00bdfe6b has its CatchHandler @ 00ae088c */
    operator_delete((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
  if ((local_d0 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
                    /* try { // try from 00adfe7c to 00bdfe8b has its CatchHandler @ 00ae06b8 */
  if ((local_f0 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
                    /* try { // try from 00adfe8c to 00bdfe97 has its CatchHandler @ 00ae069c */
  }
  if ((local_110 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_0109ff30,&PTR_LOOP_00be5ed0);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
