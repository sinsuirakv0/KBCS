# 00a8cdbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a8cdbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cdbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/reference_unresolved-0017.md#compare-10899c66ce9a9a0707724b6c096487cf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a8ce00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8c/00a8ce00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0057.md#compare-5a8508880a478eb15d517cfb82c6a286)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "0eb70a7d5f967f5058e11e230229b2fa06333f92891a65ed6054c35fa12a13f0",
  "source_text_sha256": "0eb70a7d5f967f5058e11e230229b2fa06333f92891a65ed6054c35fa12a13f0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8cdbc",
        "00a8d0fb"
      ]
    ],
    "bytes_sha256": "eb457c1842a4fef16cf21e3d4ca613a2333380c18377b50a616baa4b972d34fb",
    "instruction_count": 208,
    "instruction_bytes": 832,
    "body_bytes": 832,
    "indirect": 0,
    "unresolved": 0
  }
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
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6642 bytes

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
                __dest = (void *)_Znwm(uVar23 << 2);
              }
              piVar2 = (int *)((long)__dest + lVar19 * 4);
              piVar26 = piVar2 + 1;
              *piVar2 = iVar4;
              memcpy(__dest,__src,(long)piVar3 - (long)__src);
              *puVar1 = __dest;
              *(int **)((long)&fde_0032fb90 + lVar25) = piVar26;
              *(void **)((long)&DWORD_0032fb98 + lVar25) = (void *)((long)__dest + uVar23 * 4);
              if (__src != (void *)0x0) {
                _ZdlPv(__src);
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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8cdbc"></a> `00a8cdbc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00a8cdc0"></a> `00a8cdc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8cdc4"></a> `00a8cdc4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a8cdc8"></a> `00a8cdc8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a8cdcc"></a> `00a8cdcc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a8cdd0"></a> `00a8cdd0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a8cdd4"></a> `00a8cdd4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a8cdd8"></a> `00a8cdd8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00a8cddc"></a> `00a8cddc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00a8cde0"></a> `00a8cde0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a8cde4"></a> `00a8cde4` | `41 0b 00 54` | b.ne 0x00a8cf4c | `CONDITIONAL_JUMP`
<a id="insn-00a8cde8"></a> `00a8cde8` | `74 00 40 b9` | ldr w20,[x3] | `FALL_THROUGH`
<a id="insn-00a8cdec"></a> `00a8cdec` | `9f 06 00 31` | cmn w20,#0x1 | `FALL_THROUGH`
<a id="insn-00a8cdf0"></a> `00a8cdf0` | `e0 0a 00 54` | b.eq 0x00a8cf4c | `CONDITIONAL_JUMP`
<a id="insn-00a8cdf4"></a> `00a8cdf4` | `17 04 40 f9` | ldr x23,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a8cdf8"></a> `00a8cdf8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00a8cdfc"></a> `00a8cdfc` | `08 2c e7 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce00"></a> `00a8ce00` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a8ce04"></a> `00a8ce04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a8ce08"></a> `00a8ce08` | `3d 34 e7 97` | bl 0x00459efc | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce0c"></a> `00a8ce0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a8ce10"></a> `00a8ce10` | `5c e4 f7 97` | bl 0x00885f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce14"></a> `00a8ce14` | `d4 09 00 35` | cbnz w20,0x00a8cf4c | `CONDITIONAL_JUMP`
<a id="insn-00a8ce18"></a> `00a8ce18` | `e8 be 4c 91` | add x8,x23,#0x32f, LSL #12 | `FALL_THROUGH`
<a id="insn-00a8ce1c"></a> `00a8ce1c` | `b5 56 86 52` | mov w21,#0x32b5 | `FALL_THROUGH`
<a id="insn-00a8ce20"></a> `00a8ce20` | `13 21 2e 91` | add x19,x8,#0xb88 | `FALL_THROUGH`
<a id="insn-00a8ce24"></a> `00a8ce24` | `d7 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce28"></a> `00a8ce28` | `96 03 8f 52` | mov w22,#0x781c | `FALL_THROUGH`
<a id="insn-00a8ce2c"></a> `00a8ce2c` | `36 07 a0 72` | movk w22,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8ce30"></a> `00a8ce30` | `14 68 76 b8` | ldr w20,[x0, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8ce34"></a> `00a8ce34` | `d3 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce38"></a> `00a8ce38` | `08 74 9f 52` | mov w8,#0xfba0 | `FALL_THROUGH`
<a id="insn-00a8ce3c"></a> `00a8ce3c` | `9c 6b 9f 52` | mov w28,#0xfb5c | `FALL_THROUGH`
<a id="insn-00a8ce40"></a> `00a8ce40` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00a8ce44"></a> `00a8ce44` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8ce48"></a> `00a8ce48` | `9a 05 80 52` | mov w26,#0x2c | `FALL_THROUGH`
<a id="insn-00a8ce4c"></a> `00a8ce4c` | `1b 80 98 52` | mov w27,#0xc400 | `FALL_THROUGH`
<a id="insn-00a8ce50"></a> `00a8ce50` | `5c 06 a0 72` | movk w28,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8ce54"></a> `00a8ce54` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8ce58"></a> `00a8ce58` | `ca 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce5c"></a> `00a8ce5c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a8ce60"></a> `00a8ce60` | `c8 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ce64"></a> `00a8ce64` | `08 68 b6 b8` | ldrsw x8,[x0, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8ce68"></a> `00a8ce68` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00a8ce6c"></a> `00a8ce6c` | `08 51 3a 9b` | smaddl x8,w8,w26,x20 | `FALL_THROUGH`
<a id="insn-00a8ce70"></a> `00a8ce70` | `08 01 1b 8b` | add x8,x8,x27 | `FALL_THROUGH`
<a id="insn-00a8ce74"></a> `00a8ce74` | `09 01 19 8b` | add x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00a8ce78"></a> `00a8ce78` | `0b a9 40 39` | ldrb w11,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00a8ce7c"></a> `00a8ce7c` | `0c ad 40 39` | ldrb w12,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00a8ce80"></a> `00a8ce80` | `2a 09 40 39` | ldrb w10,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00a8ce84"></a> `00a8ce84` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00a8ce88"></a> `00a8ce88` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00a8ce8c"></a> `00a8ce8c` | `2b 0d 40 39` | ldrb w11,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00a8ce90"></a> `00a8ce90` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00a8ce94"></a> `00a8ce94` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00a8ce98"></a> `00a8ce98` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00a8ce9c"></a> `00a8ce9c` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00a8cea0"></a> `00a8cea0` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a8cea4"></a> `00a8cea4` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00a8cea8"></a> `00a8cea8` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00a8ceac"></a> `00a8ceac` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00a8ceb0"></a> `00a8ceb0` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00a8ceb4"></a> `00a8ceb4` | `54 01 08 2a` | orr w20,w10,w8 | `FALL_THROUGH`
<a id="insn-00a8ceb8"></a> `00a8ceb8` | `b2 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8cebc"></a> `00a8cebc` | `08 00 19 8b` | add x8,x0,x25 | `FALL_THROUGH`
<a id="insn-00a8cec0"></a> `00a8cec0` | `39 13 00 91` | add x25,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00a8cec4"></a> `00a8cec4` | `3f a3 00 f1` | cmp x25,#0x28 | `FALL_THROUGH`
<a id="insn-00a8cec8"></a> `00a8cec8` | `14 69 3c b8` | str w20,[x8, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cecc"></a> `00a8cecc` | `61 fc ff 54` | b.ne 0x00a8ce58 | `CONDITIONAL_JUMP`
<a id="insn-00a8ced0"></a> `00a8ced0` | `9c 03 8f 52` | mov w28,#0x781c | `FALL_THROUGH`
<a id="insn-00a8ced4"></a> `00a8ced4` | `e9 be 50 91` | add x9,x23,#0x42f, LSL #12 | `FALL_THROUGH`
<a id="insn-00a8ced8"></a> `00a8ced8` | `3c 07 a0 72` | movk w28,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8cedc"></a> `00a8cedc` | `34 a1 25 91` | add x20,x9,#0x968 | `FALL_THROUGH`
<a id="insn-00a8cee0"></a> `00a8cee0` | `e8 6a bc b8` | ldrsw x8,[x23, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cee4"></a> `00a8cee4` | `08 05 08 8b` | add x8,x8,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00a8cee8"></a> `00a8cee8` | `96 6a 68 38` | ldrb w22,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a8ceec"></a> `00a8ceec` | `a5 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8cef0"></a> `00a8cef0` | `88 70 9f 52` | mov w8,#0xfb84 | `FALL_THROUGH`
<a id="insn-00a8cef4"></a> `00a8cef4` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8cef8"></a> `00a8cef8` | `16 68 28 38` | strb w22,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a8cefc"></a> `00a8cefc` | `e8 6a bc b8` | ldrsw x8,[x23, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cf00"></a> `00a8cf00` | `08 05 08 8b` | add x8,x8,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00a8cf04"></a> `00a8cf04` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00a8cf08"></a> `00a8cf08` | `16 05 40 39` | ldrb w22,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00a8cf0c"></a> `00a8cf0c` | `9d 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8cf10"></a> `00a8cf10` | `a8 70 9f 52` | mov w8,#0xfb85 | `FALL_THROUGH`
<a id="insn-00a8cf14"></a> `00a8cf14` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8cf18"></a> `00a8cf18` | `16 68 28 38` | strb w22,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a8cf1c"></a> `00a8cf1c` | `e8 6a bc b8` | ldrsw x8,[x23, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cf20"></a> `00a8cf20` | `08 05 08 8b` | add x8,x8,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00a8cf24"></a> `00a8cf24` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00a8cf28"></a> `00a8cf28` | `14 09 40 39` | ldrb w20,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00a8cf2c"></a> `00a8cf2c` | `95 49 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a8cf30"></a> `00a8cf30` | `c8 70 9f 52` | mov w8,#0xfb86 | `FALL_THROUGH`
<a id="insn-00a8cf34"></a> `00a8cf34` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8cf38"></a> `00a8cf38` | `14 68 28 38` | strb w20,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a8cf3c"></a> `00a8cf3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00a8cf40"></a> `00a8cf40` | `e9 6a 75 38` | ldrb w9,[x23, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00a8cf44"></a> `00a8cf44` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a8cf48"></a> `00a8cf48` | `29 01 00 34` | cbz w9,0x00a8cf6c | `CONDITIONAL_JUMP`
<a id="insn-00a8cf4c"></a> `00a8cf4c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a8cf50"></a> `00a8cf50` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a8cf54"></a> `00a8cf54` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a8cf58"></a> `00a8cf58` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a8cf5c"></a> `00a8cf5c` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a8cf60"></a> `00a8cf60` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8cf64"></a> `00a8cf64` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00a8cf68"></a> `00a8cf68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a8cf6c"></a> `00a8cf6c` | `08 80 98 52` | mov w8,#0xc400 | `FALL_THROUGH`
<a id="insn-00a8cf70"></a> `00a8cf70` | `69 80 98 52` | mov w9,#0xc403 | `FALL_THROUGH`
<a id="insn-00a8cf74"></a> `00a8cf74` | `59 01 80 52` | mov w25,#0xa | `FALL_THROUGH`
<a id="insn-00a8cf78"></a> `00a8cf78` | `f4 02 08 8b` | add x20,x23,x8 | `FALL_THROUGH`
<a id="insn-00a8cf7c"></a> `00a8cf7c` | `fb 02 09 8b` | add x27,x23,x9 | `FALL_THROUGH`
<a id="insn-00a8cf80"></a> `00a8cf80` | `95 05 80 52` | mov w21,#0x2c | `FALL_THROUGH`
<a id="insn-00a8cf84"></a> `00a8cf84` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a8cf88"></a> `00a8cf88` | `06 00 00 14` | b 0x00a8cfa0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a8cf8c"></a> `00a8cf8c` | `58 47 00 b8` | str w24,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00a8cf90"></a> `00a8cf90` | `7a 06 00 f9` | str x26,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a8cf94"></a> `00a8cf94` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00a8cf98"></a> `00a8cf98` | `7b 13 00 91` | add x27,x27,#0x4 | `FALL_THROUGH`
<a id="insn-00a8cf9c"></a> `00a8cf9c` | `80 fd ff 54` | b.eq 0x00a8cf4c | `CONDITIONAL_JUMP`
<a id="insn-00a8cfa0"></a> `00a8cfa0` | `e1 6a bc b8` | ldrsw x1,[x23, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cfa4"></a> `00a8cfa4` | `e0 e2 0e 91` | add x0,x23,#0x3b8 | `FALL_THROUGH`
<a id="insn-00a8cfa8"></a> `00a8cfa8` | `28 50 35 9b` | smaddl x8,w1,w21,x20 | `FALL_THROUGH`
<a id="insn-00a8cfac"></a> `00a8cfac` | `29 6c 35 9b` | smaddl x9,w1,w21,x27 | `FALL_THROUGH`
<a id="insn-00a8cfb0"></a> `00a8cfb0` | `0b a1 40 39` | ldrb w11,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a8cfb4"></a> `00a8cfb4` | `0d a5 40 39` | ldrb w13,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00a8cfb8"></a> `00a8cfb8` | `2a d1 5f 38` | ldurb w10,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-00a8cfbc"></a> `00a8cfbc` | `2c e1 5f 38` | ldurb w12,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00a8cfc0"></a> `00a8cfc0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00a8cfc4"></a> `00a8cfc4` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00a8cfc8"></a> `00a8cfc8` | `2c f1 5f 38` | ldurb w12,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00a8cfcc"></a> `00a8cfcc` | `0d a9 40 39` | ldrb w13,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00a8cfd0"></a> `00a8cfd0` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00a8cfd4"></a> `00a8cfd4` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00a8cfd8"></a> `00a8cfd8` | `08 ad 40 39` | ldrb w8,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00a8cfdc"></a> `00a8cfdc` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00a8cfe0"></a> `00a8cfe0` | `4a 41 0b 2a` | orr w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00a8cfe4"></a> `00a8cfe4` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00a8cfe8"></a> `00a8cfe8` | `48 61 08 2a` | orr w8,w10,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00a8cfec"></a> `00a8cfec` | `02 09 00 51` | sub w2,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a8cff0"></a> `00a8cff0` | `a4 3b ec 97` | bl 0x0059be80 | `UNCONDITIONAL_CALL`
<a id="insn-00a8cff4"></a> `00a8cff4` | `00 fd 07 36` | tbz w0,#0x0,0x00a8cf94 | `CONDITIONAL_JUMP`
<a id="insn-00a8cff8"></a> `00a8cff8` | `e8 6a bc b8` | ldrsw x8,[x23, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a8cffc"></a> `00a8cffc` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00a8d000"></a> `00a8d000` | `09 51 35 9b` | smaddl x9,w8,w21,x20 | `FALL_THROUGH`
<a id="insn-00a8d004"></a> `00a8d004` | `08 6d 35 9b` | smaddl x8,w8,w21,x27 | `FALL_THROUGH`
<a id="insn-00a8d008"></a> `00a8d008` | `2b a1 40 39` | ldrb w11,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00a8d00c"></a> `00a8d00c` | `2d a5 40 39` | ldrb w13,[x9, #0x29] | `FALL_THROUGH`
<a id="insn-00a8d010"></a> `00a8d010` | `0a d1 5f 38` | ldurb w10,[x8, #-0x3] | `FALL_THROUGH`
<a id="insn-00a8d014"></a> `00a8d014` | `0c e1 5f 38` | ldurb w12,[x8, #-0x2] | `FALL_THROUGH`
<a id="insn-00a8d018"></a> `00a8d018` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00a8d01c"></a> `00a8d01c` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00a8d020"></a> `00a8d020` | `0c f1 5f 38` | ldurb w12,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00a8d024"></a> `00a8d024` | `2d a9 40 39` | ldrb w13,[x9, #0x2a] | `FALL_THROUGH`
<a id="insn-00a8d028"></a> `00a8d028` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00a8d02c"></a> `00a8d02c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00a8d030"></a> `00a8d030` | `29 ad 40 39` | ldrb w9,[x9, #0x2b] | `FALL_THROUGH`
<a id="insn-00a8d034"></a> `00a8d034` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00a8d038"></a> `00a8d038` | `4a 41 0b 2a` | orr w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00a8d03c"></a> `00a8d03c` | `29 01 08 4a` | eor w9,w9,w8 | `FALL_THROUGH`
<a id="insn-00a8d040"></a> `00a8d040` | `7a a2 40 a9` | ldp x26,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a8d044"></a> `00a8d044` | `49 61 09 2a` | orr w9,w10,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00a8d048"></a> `00a8d048` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00a8d04c"></a> `00a8d04c` | `38 09 00 51` | sub w24,w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a8d050"></a> `00a8d050` | `e3 f9 ff 54` | b.cc 0x00a8cf8c | `CONDITIONAL_JUMP`
<a id="insn-00a8d054"></a> `00a8d054` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00a8d058"></a> `00a8d058` | `55 03 14 cb` | sub x21,x26,x20 | `FALL_THROUGH`
<a id="insn-00a8d05c"></a> `00a8d05c` | `ba fe 42 93` | asr x26,x21,#0x2 | `FALL_THROUGH`
<a id="insn-00a8d060"></a> `00a8d060` | `49 07 00 91` | add x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00a8d064"></a> `00a8d064` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00a8d068"></a> `00a8d068` | `4a 04 00 b5` | cbnz x10,0x00a8d0f0 | `CONDITIONAL_JUMP`
<a id="insn-00a8d06c"></a> `00a8d06c` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00a8d070"></a> `00a8d070` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a8d074"></a> `00a8d074` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00a8d078"></a> `00a8d078` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00a8d07c"></a> `00a8d07c` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00a8d080"></a> `00a8d080` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00a8d084"></a> `00a8d084` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00a8d088"></a> `00a8d088` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00a8d08c"></a> `00a8d08c` | `fc 00 00 b4` | cbz x28,0x00a8d0a8 | `CONDITIONAL_JUMP`
<a id="insn-00a8d090"></a> `00a8d090` | `88 ff 7e d3` | lsr x8,x28,#0x3e | `FALL_THROUGH`
<a id="insn-00a8d094"></a> `00a8d094` | `28 03 00 b5` | cbnz x8,0x00a8d0f8 | `CONDITIONAL_JUMP`
<a id="insn-00a8d098"></a> `00a8d098` | `80 f7 7e d3` | lsl x0,x28,#0x2 | `FALL_THROUGH`
<a id="insn-00a8d09c"></a> `00a8d09c` | `d5 37 05 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00a8d0a0"></a> `00a8d0a0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00a8d0a4"></a> `00a8d0a4` | `02 00 00 14` | b 0x00a8d0ac | `UNCONDITIONAL_JUMP`
<a id="insn-00a8d0a8"></a> `00a8d0a8` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00a8d0ac"></a> `00a8d0ac` | `da 0a 1a 8b` | add x26,x22,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a8d0b0"></a> `00a8d0b0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a8d0b4"></a> `00a8d0b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a8d0b8"></a> `00a8d0b8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00a8d0bc"></a> `00a8d0bc` | `dc 0a 1c 8b` | add x28,x22,x28, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a8d0c0"></a> `00a8d0c0` | `58 47 00 b8` | str w24,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00a8d0c4"></a> `00a8d0c4` | `27 38 05 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00a8d0c8"></a> `00a8d0c8` | `76 6a 00 a9` | stp x22,x26,[x19] | `FALL_THROUGH`
<a id="insn-00a8d0cc"></a> `00a8d0cc` | `7c 0a 00 f9` | str x28,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a8d0d0"></a> `00a8d0d0` | `74 00 00 b4` | cbz x20,0x00a8d0dc | `CONDITIONAL_JUMP`
<a id="insn-00a8d0d4"></a> `00a8d0d4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a8d0d8"></a> `00a8d0d8` | `ce 37 05 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00a8d0dc"></a> `00a8d0dc` | `9c 03 8f 52` | mov w28,#0x781c | `FALL_THROUGH`
<a id="insn-00a8d0e0"></a> `00a8d0e0` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a8d0e4"></a> `00a8d0e4` | `95 05 80 52` | mov w21,#0x2c | `FALL_THROUGH`
<a id="insn-00a8d0e8"></a> `00a8d0e8` | `3c 07 a0 72` | movk w28,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a8d0ec"></a> `00a8d0ec` | `a9 ff ff 17` | b 0x00a8cf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00a8d0f0"></a> `00a8d0f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a8d0f4"></a> `00a8d0f4` | `1d 02 e7 97` | bl 0x0044d968 | `CALL_TERMINATOR`
<a id="insn-00a8d0f8"></a> `00a8d0f8` | `a2 44 e6 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a8cdbc`](#insn-00a8cdbc) 範囲 `[['00a8cdbc', '00a8cde7']]`
  - `CONDITIONAL_JUMP` [`00a8cde4`](#insn-00a8cde4) → [`00a8cf4c`](#insn-00a8cf4c)
  - `FALL_THROUGH` [`00a8cde4`](#insn-00a8cde4) → [`00a8cde8`](#insn-00a8cde8)
- ブロック [`00a8cde8`](#insn-00a8cde8) 範囲 `[['00a8cde8', '00a8cdf3']]`
  - `CONDITIONAL_JUMP` [`00a8cdf0`](#insn-00a8cdf0) → [`00a8cf4c`](#insn-00a8cf4c)
  - `FALL_THROUGH` [`00a8cdf0`](#insn-00a8cdf0) → [`00a8cdf4`](#insn-00a8cdf4)
- ブロック [`00a8cdf4`](#insn-00a8cdf4) 範囲 `[['00a8cdf4', '00a8ce17']]`
  - `CONDITIONAL_JUMP` [`00a8ce14`](#insn-00a8ce14) → [`00a8cf4c`](#insn-00a8cf4c)
  - `FALL_THROUGH` [`00a8ce14`](#insn-00a8ce14) → [`00a8ce18`](#insn-00a8ce18)
- ブロック [`00a8ce18`](#insn-00a8ce18) 範囲 `[['00a8ce18', '00a8ce3f']]`
  - `FALL_THROUGH` [`00a8ce3c`](#insn-00a8ce3c) → [`00a8ce40`](#insn-00a8ce40)
- ブロック [`00a8ce40`](#insn-00a8ce40) 範囲 `[['00a8ce40', '00a8ce57']]`
  - `FALL_THROUGH` [`00a8ce54`](#insn-00a8ce54) → [`00a8ce58`](#insn-00a8ce58)
- ブロック [`00a8ce58`](#insn-00a8ce58) 範囲 `[['00a8ce58', '00a8ce87']]`
  - `FALL_THROUGH` [`00a8ce84`](#insn-00a8ce84) → [`00a8ce88`](#insn-00a8ce88)
- ブロック [`00a8ce88`](#insn-00a8ce88) 範囲 `[['00a8ce88', '00a8cebb']]`
  - `FALL_THROUGH` [`00a8ceb8`](#insn-00a8ceb8) → [`00a8cebc`](#insn-00a8cebc)
- ブロック [`00a8cebc`](#insn-00a8cebc) 範囲 `[['00a8cebc', '00a8cecf']]`
  - `CONDITIONAL_JUMP` [`00a8cecc`](#insn-00a8cecc) → [`00a8ce58`](#insn-00a8ce58)
  - `FALL_THROUGH` [`00a8cecc`](#insn-00a8cecc) → [`00a8ced0`](#insn-00a8ced0)
- ブロック [`00a8ced0`](#insn-00a8ced0) 範囲 `[['00a8ced0', '00a8cefb']]`
  - `FALL_THROUGH` [`00a8cef8`](#insn-00a8cef8) → [`00a8cefc`](#insn-00a8cefc)
- ブロック [`00a8cefc`](#insn-00a8cefc) 範囲 `[['00a8cefc', '00a8cf17']]`
  - `FALL_THROUGH` [`00a8cf14`](#insn-00a8cf14) → [`00a8cf18`](#insn-00a8cf18)
- ブロック [`00a8cf18`](#insn-00a8cf18) 範囲 `[['00a8cf18', '00a8cf4b']]`
  - `CONDITIONAL_JUMP` [`00a8cf48`](#insn-00a8cf48) → [`00a8cf6c`](#insn-00a8cf6c)
  - `FALL_THROUGH` [`00a8cf48`](#insn-00a8cf48) → [`00a8cf4c`](#insn-00a8cf4c)
- ブロック [`00a8cf4c`](#insn-00a8cf4c) 範囲 `[['00a8cf4c', '00a8cf6b']]`
- ブロック [`00a8cf6c`](#insn-00a8cf6c) 範囲 `[['00a8cf6c', '00a8cf8b']]`
  - `UNCONDITIONAL_JUMP` [`00a8cf88`](#insn-00a8cf88) → [`00a8cfa0`](#insn-00a8cfa0)
- ブロック [`00a8cf8c`](#insn-00a8cf8c) 範囲 `[['00a8cf8c', '00a8cf8f']]`
  - `FALL_THROUGH` [`00a8cf8c`](#insn-00a8cf8c) → [`00a8cf90`](#insn-00a8cf90)
- ブロック [`00a8cf90`](#insn-00a8cf90) 範囲 `[['00a8cf90', '00a8cf93']]`
  - `FALL_THROUGH` [`00a8cf90`](#insn-00a8cf90) → [`00a8cf94`](#insn-00a8cf94)
- ブロック [`00a8cf94`](#insn-00a8cf94) 範囲 `[['00a8cf94', '00a8cf9f']]`
  - `CONDITIONAL_JUMP` [`00a8cf9c`](#insn-00a8cf9c) → [`00a8cf4c`](#insn-00a8cf4c)
  - `FALL_THROUGH` [`00a8cf9c`](#insn-00a8cf9c) → [`00a8cfa0`](#insn-00a8cfa0)
- ブロック [`00a8cfa0`](#insn-00a8cfa0) 範囲 `[['00a8cfa0', '00a8cfb3']]`
  - `FALL_THROUGH` [`00a8cfb0`](#insn-00a8cfb0) → [`00a8cfb4`](#insn-00a8cfb4)
- ブロック [`00a8cfb4`](#insn-00a8cfb4) 範囲 `[['00a8cfb4', '00a8cff7']]`
  - `CONDITIONAL_JUMP` [`00a8cff4`](#insn-00a8cff4) → [`00a8cf94`](#insn-00a8cf94)
  - `FALL_THROUGH` [`00a8cff4`](#insn-00a8cff4) → [`00a8cff8`](#insn-00a8cff8)
- ブロック [`00a8cff8`](#insn-00a8cff8) 範囲 `[['00a8cff8', '00a8cfff']]`
  - `FALL_THROUGH` [`00a8cffc`](#insn-00a8cffc) → [`00a8d000`](#insn-00a8d000)
- ブロック [`00a8d000`](#insn-00a8d000) 範囲 `[['00a8d000', '00a8d053']]`
  - `CONDITIONAL_JUMP` [`00a8d050`](#insn-00a8d050) → [`00a8cf8c`](#insn-00a8cf8c)
  - `FALL_THROUGH` [`00a8d050`](#insn-00a8d050) → [`00a8d054`](#insn-00a8d054)
- ブロック [`00a8d054`](#insn-00a8d054) 範囲 `[['00a8d054', '00a8d06b']]`
  - `CONDITIONAL_JUMP` [`00a8d068`](#insn-00a8d068) → [`00a8d0f0`](#insn-00a8d0f0)
  - `FALL_THROUGH` [`00a8d068`](#insn-00a8d068) → [`00a8d06c`](#insn-00a8d06c)
- ブロック [`00a8d06c`](#insn-00a8d06c) 範囲 `[['00a8d06c', '00a8d08f']]`
  - `CONDITIONAL_JUMP` [`00a8d08c`](#insn-00a8d08c) → [`00a8d0a8`](#insn-00a8d0a8)
  - `FALL_THROUGH` [`00a8d08c`](#insn-00a8d08c) → [`00a8d090`](#insn-00a8d090)
- ブロック [`00a8d090`](#insn-00a8d090) 範囲 `[['00a8d090', '00a8d097']]`
  - `CONDITIONAL_JUMP` [`00a8d094`](#insn-00a8d094) → [`00a8d0f8`](#insn-00a8d0f8)
  - `FALL_THROUGH` [`00a8d094`](#insn-00a8d094) → [`00a8d098`](#insn-00a8d098)
- ブロック [`00a8d098`](#insn-00a8d098) 範囲 `[['00a8d098', '00a8d0a7']]`
  - `UNCONDITIONAL_JUMP` [`00a8d0a4`](#insn-00a8d0a4) → [`00a8d0ac`](#insn-00a8d0ac)
- ブロック [`00a8d0a8`](#insn-00a8d0a8) 範囲 `[['00a8d0a8', '00a8d0ab']]`
  - `FALL_THROUGH` [`00a8d0a8`](#insn-00a8d0a8) → [`00a8d0ac`](#insn-00a8d0ac)
- ブロック [`00a8d0ac`](#insn-00a8d0ac) 範囲 `[['00a8d0ac', '00a8d0d3']]`
  - `CONDITIONAL_JUMP` [`00a8d0d0`](#insn-00a8d0d0) → [`00a8d0dc`](#insn-00a8d0dc)
  - `FALL_THROUGH` [`00a8d0d0`](#insn-00a8d0d0) → [`00a8d0d4`](#insn-00a8d0d4)
- ブロック [`00a8d0d4`](#insn-00a8d0d4) 範囲 `[['00a8d0d4', '00a8d0db']]`
  - `FALL_THROUGH` [`00a8d0d8`](#insn-00a8d0d8) → [`00a8d0dc`](#insn-00a8d0dc)
- ブロック [`00a8d0dc`](#insn-00a8d0dc) 範囲 `[['00a8d0dc', '00a8d0df']]`
  - `FALL_THROUGH` [`00a8d0dc`](#insn-00a8d0dc) → [`00a8d0e0`](#insn-00a8d0e0)
- ブロック [`00a8d0e0`](#insn-00a8d0e0) 範囲 `[['00a8d0e0', '00a8d0ef']]`
  - `UNCONDITIONAL_JUMP` [`00a8d0ec`](#insn-00a8d0ec) → [`00a8cf90`](#insn-00a8cf90)
- ブロック [`00a8d0f0`](#insn-00a8d0f0) 範囲 `[['00a8d0f0', '00a8d0f7']]`
- ブロック [`00a8d0f8`](#insn-00a8d0f8) 範囲 `[['00a8d0f8', '00a8d0fb']]`

## 命令位置別の参照

- [`00a8cdc0`](#insn-00a8cdc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdc4`](#insn-00a8cdc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdc8`](#insn-00a8cdc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdcc`](#insn-00a8cdcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdd0`](#insn-00a8cdd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdd4`](#insn-00a8cdd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cde4`](#insn-00a8cde4) → [`00a8cf4c`](#insn-00a8cf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdf0`](#insn-00a8cdf0) → [`00a8cf4c`](#insn-00a8cf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cdfc`](#insn-00a8cdfc) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce08`](#insn-00a8ce08) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce10`](#insn-00a8ce10) → [`00885f80`](../00885/00885f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00885f80` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce14`](#insn-00a8ce14) → [`00a8cf4c`](#insn-00a8cf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce24`](#insn-00a8ce24) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce30`](#insn-00a8ce30) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8ce34`](#insn-00a8ce34) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce54`](#insn-00a8ce54) → `0032fba0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a8ce58`](#insn-00a8ce58) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce60`](#insn-00a8ce60) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8ce64`](#insn-00a8ce64) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8ceb8`](#insn-00a8ceb8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8cec8`](#insn-00a8cec8) → `0032fb5c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a8cecc`](#insn-00a8cecc) → [`00a8ce58`](#insn-00a8ce58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cee0`](#insn-00a8cee0) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8ceec`](#insn-00a8ceec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8cef8`](#insn-00a8cef8) → `0032fb84`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a8cefc`](#insn-00a8cefc) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8cf0c`](#insn-00a8cf0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf18`](#insn-00a8cf18) → `0032fb85`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a8cf1c`](#insn-00a8cf1c) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8cf2c`](#insn-00a8cf2c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf38`](#insn-00a8cf38) → `0032fb86`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a8cf3c`](#insn-00a8cf3c) → `0032fb88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a8cf44`](#insn-00a8cf44) → `0032fb90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032fb90` · 推定型 `dword`
- [`00a8cf48`](#insn-00a8cf48) → [`00a8cf6c`](#insn-00a8cf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf4c`](#insn-00a8cf4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf50`](#insn-00a8cf50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf54`](#insn-00a8cf54) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf58`](#insn-00a8cf58) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf5c`](#insn-00a8cf5c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf60`](#insn-00a8cf60) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf84`](#insn-00a8cf84) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf88`](#insn-00a8cf88) → [`00a8cfa0`](#insn-00a8cfa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cf90`](#insn-00a8cf90) → `0032fb90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032fb90` · 推定型 `dword`
- [`00a8cf9c`](#insn-00a8cf9c) → [`00a8cf4c`](#insn-00a8cf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cfa0`](#insn-00a8cfa0) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8cff0`](#insn-00a8cff0) → [`0059be80`](../0059b/0059be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0059be80` · 推定シンボル `None` · 推定型 `None`
- [`00a8cff4`](#insn-00a8cff4) → [`00a8cf94`](#insn-00a8cf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8cff8`](#insn-00a8cff8) → `0039781c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a8d040`](#insn-00a8d040) → `0032fb90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032fb90` · 推定型 `dword`
- [`00a8d040`](#insn-00a8d040) → `0032fb98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a8d050`](#insn-00a8d050) → [`00a8cf8c`](#insn-00a8cf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d054`](#insn-00a8d054) → `0032fb88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a8d068`](#insn-00a8d068) → [`00a8d0f0`](#insn-00a8d0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d08c`](#insn-00a8d08c) → [`00a8d0a8`](#insn-00a8d0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d094`](#insn-00a8d094) → [`00a8d0f8`](#insn-00a8d0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d09c`](#insn-00a8d09c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0a4`](#insn-00a8d0a4) → [`00a8d0ac`](#insn-00a8d0ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0c4`](#insn-00a8d0c4) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0c8`](#insn-00a8d0c8) → `0032fb88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a8d0c8`](#insn-00a8d0c8) → `0032fb90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0032fb90` · 推定型 `dword`
- [`00a8d0cc`](#insn-00a8d0cc) → `0032fb98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a8d0d0`](#insn-00a8d0d0) → [`00a8d0dc`](#insn-00a8d0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0d8`](#insn-00a8d0d8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0e0`](#insn-00a8d0e0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0ec`](#insn-00a8d0ec) → [`00a8cf90`](#insn-00a8cf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0f4`](#insn-00a8d0f4) → [`0044d968`](../0044d/0044d968.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044d968` · 推定シンボル `None` · 推定型 `None`
- [`00a8d0f8`](#insn-00a8d0f8) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8cdc0`](#insn-00a8cdc0)

~~~json
{
  "source": "00a8cdc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdc4`](#insn-00a8cdc4)

~~~json
{
  "source": "00a8cdc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdc8`](#insn-00a8cdc8)

~~~json
{
  "source": "00a8cdc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdcc`](#insn-00a8cdcc)

~~~json
{
  "source": "00a8cdcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdd0`](#insn-00a8cdd0)

~~~json
{
  "source": "00a8cdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdd4`](#insn-00a8cdd4)

~~~json
{
  "source": "00a8cdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cde4`](#insn-00a8cde4)

~~~json
{
  "source": "00a8cde4",
  "target": "00a8cf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdf0`](#insn-00a8cdf0)

~~~json
{
  "source": "00a8cdf0",
  "target": "00a8cf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cdfc`](#insn-00a8cdfc)

~~~json
{
  "source": "00a8cdfc",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce08`](#insn-00a8ce08)

~~~json
{
  "source": "00a8ce08",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce10`](#insn-00a8ce10)

~~~json
{
  "source": "00a8ce10",
  "target": "00885f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce14`](#insn-00a8ce14)

~~~json
{
  "source": "00a8ce14",
  "target": "00a8cf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8ce24`](#insn-00a8ce24)

~~~json
{
  "source": "00a8ce24",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce30`](#insn-00a8ce30)

~~~json
{
  "source": "00a8ce30",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8ce34`](#insn-00a8ce34)

~~~json
{
  "source": "00a8ce34",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce54`](#insn-00a8ce54)

~~~json
{
  "source": "00a8ce54",
  "target": "0032fba0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb9c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0032fb9c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8ce58`](#insn-00a8ce58)

~~~json
{
  "source": "00a8ce58",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce60`](#insn-00a8ce60)

~~~json
{
  "source": "00a8ce60",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ce64`](#insn-00a8ce64)

~~~json
{
  "source": "00a8ce64",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8ceb8`](#insn-00a8ceb8)

~~~json
{
  "source": "00a8ceb8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8cec8`](#insn-00a8cec8)

~~~json
{
  "source": "00a8cec8",
  "target": "0032fb5c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb51",
  "offset": 11,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032fb51",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cecc`](#insn-00a8cecc)

~~~json
{
  "source": "00a8cecc",
  "target": "00a8ce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cee0`](#insn-00a8cee0)

~~~json
{
  "source": "00a8cee0",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8ceec`](#insn-00a8ceec)

~~~json
{
  "source": "00a8ceec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8cef8`](#insn-00a8cef8)

~~~json
{
  "source": "00a8cef8",
  "target": "0032fb84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb84",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "e4441100",
  "capture_start": "0032fb84",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cefc`](#insn-00a8cefc)

~~~json
{
  "source": "00a8cefc",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf0c`](#insn-00a8cf0c)

~~~json
{
  "source": "00a8cf0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8cf18`](#insn-00a8cf18)

~~~json
{
  "source": "00a8cf18",
  "target": "0032fb85",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb84",
  "offset": 1,
  "size": 4,
  "datatype": "dword",
  "bytes": "e4441100",
  "capture_start": "0032fb84",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf1c`](#insn-00a8cf1c)

~~~json
{
  "source": "00a8cf1c",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf2c`](#insn-00a8cf2c)

~~~json
{
  "source": "00a8cf2c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8cf38`](#insn-00a8cf38)

~~~json
{
  "source": "00a8cf38",
  "target": "0032fb86",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb84",
  "offset": 2,
  "size": 4,
  "datatype": "dword",
  "bytes": "e4441100",
  "capture_start": "0032fb84",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf3c`](#insn-00a8cf3c)

~~~json
{
  "source": "00a8cf3c",
  "target": "0032fb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb88",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0032fb88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf44`](#insn-00a8cf44)

~~~json
{
  "source": "00a8cf44",
  "target": "0032fb90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb90",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032fb90",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf48`](#insn-00a8cf48)

~~~json
{
  "source": "00a8cf48",
  "target": "00a8cf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf4c`](#insn-00a8cf4c)

~~~json
{
  "source": "00a8cf4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf50`](#insn-00a8cf50)

~~~json
{
  "source": "00a8cf50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf54`](#insn-00a8cf54)

~~~json
{
  "source": "00a8cf54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf58`](#insn-00a8cf58)

~~~json
{
  "source": "00a8cf58",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf5c`](#insn-00a8cf5c)

~~~json
{
  "source": "00a8cf5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf60`](#insn-00a8cf60)

~~~json
{
  "source": "00a8cf60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf84`](#insn-00a8cf84)

~~~json
{
  "source": "00a8cf84",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf88`](#insn-00a8cf88)

~~~json
{
  "source": "00a8cf88",
  "target": "00a8cfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cf90`](#insn-00a8cf90)

~~~json
{
  "source": "00a8cf90",
  "target": "0032fb90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb90",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032fb90",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cf9c`](#insn-00a8cf9c)

~~~json
{
  "source": "00a8cf9c",
  "target": "00a8cf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cfa0`](#insn-00a8cfa0)

~~~json
{
  "source": "00a8cfa0",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8cff0`](#insn-00a8cff0)

~~~json
{
  "source": "00a8cff0",
  "target": "0059be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8cff4`](#insn-00a8cff4)

~~~json
{
  "source": "00a8cff4",
  "target": "00a8cf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8cff8`](#insn-00a8cff8)

~~~json
{
  "source": "00a8cff8",
  "target": "0039781c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039781c",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039781c",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d040`](#insn-00a8d040)

~~~json
{
  "source": "00a8d040",
  "target": "0032fb90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb90",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032fb90",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d040`](#insn-00a8d040)

~~~json
{
  "source": "00a8d040",
  "target": "0032fb98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb98",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "d4441100",
  "capture_start": "0032fb98",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d050`](#insn-00a8d050)

~~~json
{
  "source": "00a8d050",
  "target": "00a8cf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d054`](#insn-00a8d054)

~~~json
{
  "source": "00a8d054",
  "target": "0032fb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb88",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0032fb88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d068`](#insn-00a8d068)

~~~json
{
  "source": "00a8d068",
  "target": "00a8d0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d08c`](#insn-00a8d08c)

~~~json
{
  "source": "00a8d08c",
  "target": "00a8d0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d094`](#insn-00a8d094)

~~~json
{
  "source": "00a8d094",
  "target": "00a8d0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d09c`](#insn-00a8d09c)

~~~json
{
  "source": "00a8d09c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8d0a4`](#insn-00a8d0a4)

~~~json
{
  "source": "00a8d0a4",
  "target": "00a8d0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d0c4`](#insn-00a8d0c4)

~~~json
{
  "source": "00a8d0c4",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8d0c8`](#insn-00a8d0c8)

~~~json
{
  "source": "00a8d0c8",
  "target": "0032fb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb88",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0032fb88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d0c8`](#insn-00a8d0c8)

~~~json
{
  "source": "00a8d0c8",
  "target": "0032fb90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb90",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0032fb90",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d0cc`](#insn-00a8d0cc)

~~~json
{
  "source": "00a8d0cc",
  "target": "0032fb98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fb98",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "d4441100",
  "capture_start": "0032fb98",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a8d0d0`](#insn-00a8d0d0)

~~~json
{
  "source": "00a8d0d0",
  "target": "00a8d0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d0d8`](#insn-00a8d0d8)

~~~json
{
  "source": "00a8d0d8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8d0e0`](#insn-00a8d0e0)

~~~json
{
  "source": "00a8d0e0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d0ec`](#insn-00a8d0ec)

~~~json
{
  "source": "00a8d0ec",
  "target": "00a8cf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8d0f4`](#insn-00a8d0f4)

~~~json
{
  "source": "00a8d0f4",
  "target": "0044d968",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8d0f8`](#insn-00a8d0f8)

~~~json
{
  "source": "00a8d0f8",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
