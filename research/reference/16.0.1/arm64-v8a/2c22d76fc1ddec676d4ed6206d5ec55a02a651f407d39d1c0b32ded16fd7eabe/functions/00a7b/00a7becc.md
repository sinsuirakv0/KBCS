# 00a7becc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00a7becc",
  "name": "FUN_00a7becc",
  "size": 460,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1129fd49fd5aa040a5b90aa8c76493bb3c53d93a97b65e78ced25cc0c81c3c7b",
  "source_text_sha256": "1129fd49fd5aa040a5b90aa8c76493bb3c53d93a97b65e78ced25cc0c81c3c7b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [0048ce50](../0048c/0048ce50.md)
- [0048ce54](../0048c/0048ce54.md)
- [008b7a10](../008b7/008b7a10.md)
- [008ba868](../008ba/008ba868.md)
- [00a7c188](../00a7c/00a7c188.md)
- [00a7c18c](../00a7c/00a7c18c.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 関連文字列（未確認候補）

~~~text
"network_unavailable"
~~~

## 疑似コード / UTF-8 3796 bytes

~~~c

void FUN_00a7becc(long param_1,undefined8 param_2,int *param_3)

{
  undefined1 *puVar1;
  int iVar2;
  long lVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined ***pppuVar6;
  undefined8 uVar7;
  long lVar8;
  byte local_a0;
  char local_9f [8];
  undefined7 uStack_97;
  undefined4 uStack_90;
  uint uStack_8c;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
  lVar3 = tpidr_el0;
                    /* try { // try from 00a7bee4 to 00b7bef7 has its CatchHandler @ 00a7c2d8 */
  local_38 = *(long *)(lVar3 + 0x28);
  iVar2 = *param_3;
  lVar8 = *(long *)(param_1 + 8);
  if (iVar2 == 4) {
    uVar5 = thunk_FUN_004978d0();
    if ((uVar5 & 1) != 0) {
      *(undefined4 *)(lVar8 + 0x3478) = 0x26;
      *(undefined4 *)((long)&DWORD_0039b1b4 + lVar8) = 2;
      if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 00a7bf9c to 00b7bfaf has its CatchHandler @ 00a7c334 */
                    /* try { // try from 00a7bfb4 to 00b7c00b has its CatchHandler @ 00a7c38c */
        FUN_008b7a10(lVar8 + 0x2f38,0);
        return;
      }
      goto LAB_00a7c0e4;
    }
    local_a0 = 0x26;
    uStack_97 = (undefined7)s_network_unavailable_002b4baa._8_8_;
    uStack_90 = CONCAT31(0x656c62,SUB81(s_network_unavailable_002b4baa._8_8_,7));
    local_9f[0] = s_network_unavailable_002b4baa[0];
    local_9f[1] = s_network_unavailable_002b4baa[1];
    local_9f[2] = s_network_unavailable_002b4baa[2];
    local_9f[3] = s_network_unavailable_002b4baa[3];
    local_9f[4] = s_network_unavailable_002b4baa[4];
    local_9f[5] = s_network_unavailable_002b4baa[5];
    local_9f[6] = s_network_unavailable_002b4baa[6];
    local_9f[7] = s_network_unavailable_002b4baa[7];
    uStack_8c = uStack_8c & 0xffffff00;
    FUN_0048ce54(local_88,&local_a0);
    local_70[0] = &PTR_FUN_00c8bb70;
    local_50 = local_70;
    FUN_008ba868(lVar8 + 0x2f08,local_88,0,0,0x24,local_70);
    if (local_50 == local_70) {
      lVar8 = 0x20;
      pppuVar6 = local_70;
LAB_00a7c044:
      (**(code **)((long)*pppuVar6 + lVar8))();
    }
    else if (local_50 != (undefined ***)0x0) {
                    /* try { // try from 00a7c034 to 00b7c03b has its CatchHandler @ 00a7c2c0 */
      lVar8 = 0x28;
      pppuVar6 = local_50;
      goto LAB_00a7c044;
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
                    /* try { // try from 00a7c060 to 00b7c067 has its CatchHandler @ 00a7c2a0 */
    if ((local_a0 & 1) != 0) {
                    /* try { // try from 00a7c068 to 00b7c087 has its CatchHandler @ 00a7c2fc */
      _ZdlPv((void *)CONCAT44(uStack_8c,uStack_90));
    }
  }
  else {
                    /* try { // try from 00a7befc to 00b7bf0f has its CatchHandler @ 00a7c2f4 */
    puVar1 = (undefined1 *)((long)&fde_table_entry_0033e360.initial_loc + lVar8);
    if (iVar2 == 3) {
      *puVar1 = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar8) = 0;
      uVar4 = FUN_0047acf4();
                    /* try { // try from 00a7bf48 to 00b7bf57 has its CatchHandler @ 00a7c2d4 */
      if (*(long *)(lVar3 + 0x28) != local_38) goto LAB_00a7c0e4;
      uVar7 = 0xb;
LAB_00a7bf54:
                    /* try { // try from 00a7bf58 to 00b7bf67 has its CatchHandler @ 00a7c2d0 */
      FUN_0047cdd4(uVar4,uVar7,0);
      return;
    }
    if (iVar2 == 0) {
      *puVar1 = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar8) = 0;
      uVar4 = FUN_0047acf4();
      if (*(long *)(lVar3 + 0x28) != local_38) goto LAB_00a7c0e4;
      uVar7 = 10;
      goto LAB_00a7bf54;
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
LAB_00a7c0e4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
