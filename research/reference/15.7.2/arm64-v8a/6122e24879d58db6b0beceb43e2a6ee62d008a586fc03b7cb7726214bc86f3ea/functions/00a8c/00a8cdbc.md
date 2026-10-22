# 00a8cdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a8cdbc.md)

## 関数情報

~~~json
{
  "address": "00a8cdbc",
  "name": "FUN_00a8cdbc",
  "size": 832,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dff0e7470992427f6dbf6c56b7f152b887f9939e1a0d8d900b0a46c4ed4d2c59",
  "source_text_sha256": "dff0e7470992427f6dbf6c56b7f152b887f9939e1a0d8d900b0a46c4ed4d2c59"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [0044d968](../0044d/0044d968.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [0059be80](../0059b/0059be80.md)
- [0081f580](../0081f/0081f580.md)
- [00885f80](../00885/00885f80.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード 1/1 / UTF-8 6811 bytes

~~~c

void FUN_00a8cdbc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 *puVar1;
  int *piVar2;
  int *piVar3;
  int iVar4;
  undefined4 uVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  byte bVar12;
  byte bVar13;
  undefined1 uVar14;
  char cVar15;
  undefined8 uVar16;
  long lVar17;
  long lVar18;
  long lVar19;
  ulong uVar20;
  void *__dest;
  ulong uVar21;
  byte *pbVar22;
  ulong uVar23;
  undefined8 uVar24;
  void *__src;
  long lVar25;
  int *piVar26;
  
  if ((*param_3 == 2) && (iVar4 = *param_4, iVar4 != -1)) {
    lVar25 = *(long *)(param_1 + 8);
    uVar24 = *param_2;
    uVar16 = FUN_00457e1c();
    FUN_00459efc(uVar16,0xb,0);
    FUN_00885f80(uVar24);
    if (iVar4 == 0) {
      puVar1 = (undefined8 *)((long)&QWORD_0032fb88 + lVar25);
      lVar17 = FUN_0081f580();
      uVar5 = *(undefined4 *)(&uleb128_0039781c + lVar17);
      lVar18 = FUN_0081f580();
                    /* try { // try from 00a8ce40 to 00b8ce87 has its CatchHandler @ 00a8ce40
                       catch() { ... } // from try @ 00a8ce40 with catch @ 00a8ce40
                       catch() { ... } // from try @ 00a8cfb4 with catch @ 00a8ce40
                       catch() { ... } // from try @ 00a8d100 with catch @ 00a8ce40 */
      lVar17 = 0;
      *(undefined4 *)((long)&QWORD_0032fb9c + lVar18 + 4) = uVar5;
      do {
        lVar18 = FUN_0081f580();
        lVar19 = FUN_0081f580();
        lVar18 = lVar18 + (long)*(int *)(&uleb128_0039781c + lVar19) * 0x2c;
        pbVar22 = (byte *)(lVar18 + 0xc400 + lVar17);
        bVar6 = *(byte *)(lVar18 + 0xc42a);
        bVar7 = *(byte *)(lVar18 + 0xc42b);
        bVar8 = pbVar22[2];
        bVar9 = pbVar22[1];
                    /* try { // try from 00a8ce88 to 00b8ce8f has its CatchHandler @ 00a8d11c */
        bVar10 = pbVar22[3];
        bVar11 = *pbVar22;
        bVar12 = *(byte *)(lVar18 + 0xc429);
        bVar13 = *(byte *)(lVar18 + 0xc428);
        lVar18 = FUN_0081f580();
                    /* try { // try from 00a8cebc to 00b8cecf has its CatchHandler @ 00a8d104 */
        lVar18 = lVar18 + lVar17;
        lVar17 = lVar17 + 4;
        *(uint *)(BYTE_ARRAY_0032fb51 + lVar18 + 0xb) =
             (uint)(bVar6 ^ bVar8) << 0x10 | (uint)(bVar7 ^ bVar10) << 0x18 |
             (uint)(bVar12 ^ bVar9) << 8 | (uint)(bVar13 ^ bVar11);
      } while (lVar17 != 0x28);
      lVar17 = lVar25 + 0x42f968;
      uVar14 = *(undefined1 *)(lVar17 + (long)*(int *)(&uleb128_0039781c + lVar25) * 3);
      lVar18 = FUN_0081f580();
      *(undefined1 *)((long)&DWORD_0032fb84 + lVar18) = uVar14;
                    /* try { // try from 00a8cefc to 00b8cf13 has its CatchHandler @ 00a8d124 */
      uVar14 = *(undefined1 *)(lVar17 + (long)*(int *)(&uleb128_0039781c + lVar25) * 3 + 1);
      lVar18 = FUN_0081f580();
                    /* try { // try from 00a8cf18 to 00b8cfb3 has its CatchHandler @ 00a8d128 */
      *(undefined1 *)((long)&DWORD_0032fb84 + lVar18 + 1) = uVar14;
      uVar14 = *(undefined1 *)(lVar17 + (long)*(int *)(&uleb128_0039781c + lVar25) * 3 + 2);
      lVar17 = FUN_0081f580();
      *(undefined1 *)((long)&DWORD_0032fb84 + lVar17 + 2) = uVar14;
      cVar15 = *(char *)(lVar25 + 0x32b5);
      *(undefined8 *)((long)&fde_0032fb90 + lVar25) = *puVar1;
      if (cVar15 == '\0') {
        lVar18 = 10;
        lVar17 = lVar25 + 0xc403;
        do {
          iVar4 = *(int *)(&uleb128_0039781c + lVar25);
          lVar19 = lVar25 + 0xc400 + (long)iVar4 * 0x2c;
          pbVar22 = (byte *)(lVar17 + (long)iVar4 * 0x2c);
                    /* try { // try from 00a8cfb4 to 00b8cfff has its CatchHandler @ 00a8ce40 */
          uVar20 = FUN_0059be80(lVar25 + 0x3b8,(long)iVar4,
                                CONCAT13(*(byte *)(lVar19 + 0x2b) ^ *pbVar22,
                                         CONCAT12(*(byte *)(lVar19 + 0x2a) ^ pbVar22[-1],
                                                  CONCAT11(*(byte *)(lVar19 + 0x29) ^ pbVar22[-2],
                                                           *(byte *)(lVar19 + 0x28) ^ pbVar22[-3])))
                                + -2);
          if ((uVar20 & 1) != 0) {
                    /* try { // try from 00a8d000 to 00b8d007 has its CatchHandler @ 00a8d100 */
            lVar19 = lVar25 + 0xc400 + (long)*(int *)(&uleb128_0039781c + lVar25) * 0x2c;
            pbVar22 = (byte *)(lVar17 + (long)*(int *)(&uleb128_0039781c + lVar25) * 0x2c);
            piVar3 = *(int **)((long)&fde_0032fb90 + lVar25);
            iVar4 = CONCAT13(*(byte *)(lVar19 + 0x2b) ^ *pbVar22,
                             CONCAT12(*(byte *)(lVar19 + 0x2a) ^ pbVar22[-1],
                                      CONCAT11(*(byte *)(lVar19 + 0x29) ^ pbVar22[-2],
                                               *(byte *)(lVar19 + 0x28) ^ pbVar22[-3]))) + -2;
            if (piVar3 < *(int **)((long)&DWORD_0032fb98 + lVar25)) {
              piVar26 = piVar3 + 1;
              *piVar3 = iVar4;
            }
            else {
              __src = (void *)*puVar1;
              lVar19 = (long)piVar3 - (long)__src >> 2;
              uVar20 = lVar19 + 1;
              if (uVar20 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_0044d968(puVar1);
              }
              uVar21 = (long)*(int **)((long)&DWORD_0032fb98 + lVar25) - (long)__src;
              uVar23 = (long)uVar21 >> 1;
              if (uVar23 <= uVar20) {
                uVar23 = uVar20;
              }
              if (0x7ffffffffffffffb < uVar21) {
                uVar23 = 0x3fffffffffffffff;
              }
              if (uVar23 == 0) {
                __dest = (void *)0x0;
              }
              else {
                if (uVar23 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                  FUN_0041e380();
                }
                __dest = operator_new(uVar23 << 2);
              }
              piVar2 = (int *)((long)__dest + lVar19 * 4);
              piVar26 = piVar2 + 1;
              *piVar2 = iVar4;
              memcpy(__dest,__src,(long)piVar3 - (long)__src);
              *puVar1 = __dest;
              *(int **)((long)&fde_0032fb90 + lVar25) = piVar26;
              *(void **)((long)&DWORD_0032fb98 + lVar25) = (void *)((long)__dest + uVar23 * 4);
              if (__src != (void *)0x0) {
                operator_delete(__src);
              }
            }
            *(int **)((long)&fde_0032fb90 + lVar25) = piVar26;
          }
          lVar18 = lVar18 + -1;
          lVar17 = lVar17 + 4;
        } while (lVar18 != 0);
      }
    }
  }
  return;
}

~~~
