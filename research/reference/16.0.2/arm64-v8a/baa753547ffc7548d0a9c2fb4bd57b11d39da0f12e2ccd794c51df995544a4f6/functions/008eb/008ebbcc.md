# 008ebbcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008ebb78`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008ebb78.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0053.md#compare-a8aec3ee7144d10671d436fb84468b56)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008ecb78`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecb78.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0054.md#compare-52913e3280d9453dd27f52e5d3fc6df1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ebbcc",
  "name": "FUN_008ebbcc",
  "size": 684,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af46dc826c17eb065ec043a5570cec618bada9d5355cce2b6d4977fce0c5e51a",
  "source_text_sha256": "af46dc826c17eb065ec043a5570cec618bada9d5355cce2b6d4977fce0c5e51a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008ebbcc",
        "008ebe73"
      ],
      [
        "008ebec4",
        "008ebec7"
      ]
    ],
    "bytes_sha256": "2773c92a56ed56c82d1f21eb648b8e019794d7372c22b7e925ae133e37c82d53",
    "instruction_count": 171,
    "instruction_bytes": 684,
    "body_bytes": 684,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008f67b8](../008f6/008f67b8.md)

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [0048795c](../00487/0048795c.md)
- [0048797c](../00487/0048797c.md)
- [00487e60](../00487/00487e60.md)
- [00488698](../00488/00488698.md)
- [008f8a40](../008f8/008f8a40.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)
- [00c580d0](../00c58/00c580d0.md)

## 関連文字列（未確認候補）

~~~text
"nyankoPictureBookData_CharaGet.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5320 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_008ebbcc(byte *param_1)

{
  ulong uVar1;
  ulong *puVar2;
  ulong *puVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined *puVar9;
  ulong uVar10;
  long lVar11;
  void *__dest;
  ulong uVar12;
  ulong uVar13;
  byte *pbVar14;
  void *__src;
  long lVar15;
  ulong *puVar16;
  ulong local_1e0;
  undefined8 uStack_1d8;
  char *local_1d0;
  undefined **local_1c8;
  void *local_1c0;
  void *local_1b8;
  byte local_1a8;
  void *local_198;
  long local_180;
  undefined *local_178 [8];
  byte local_138;
  void *local_128;
  undefined1 auStack_110 [160];
  long local_70;
  
  lVar4 = tpidr_el0;
  local_70 = *(long *)(lVar4 + 0x28);
  if ((*param_1 & 1) == 0) {
    *param_1 = 1;
    FUN_00487e60(&local_1c8);
    pbVar14 = param_1 + 8;
    local_1c8 = &PTR_FUN_00c64e08;
    *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)pbVar14;
                    /* try { // try from 008ebc34 to 009ebccb has its CatchHandler @ 008df140 */
    local_1d0 = (char *)_Znwm(0x28);
    uStack_1d8 = _UNK_002c32e8;
    local_1e0 = _DAT_002c32e0;
    uVar8 = s_nyankoPictureBookData_CharaGet_c_002a49e2._24_8_;
    uVar7 = s_nyankoPictureBookData_CharaGet_c_002a49e2._16_8_;
    uVar6 = s_nyankoPictureBookData_CharaGet_c_002a49e2._8_8_;
    uVar5 = s_nyankoPictureBookData_CharaGet_c_002a49e2._0_8_;
    local_1d0[0x20] = 's';
    local_1d0[0x21] = 'v';
    *(undefined8 *)(local_1d0 + 8) = uVar6;
    *(undefined8 *)local_1d0 = uVar5;
    *(undefined8 *)(local_1d0 + 0x18) = uVar8;
    *(undefined8 *)(local_1d0 + 0x10) = uVar7;
    local_1d0[0x22] = '\0';
    uVar10 = FUN_00b11188(&local_1c8,&local_1e0,0,0);
    if ((local_1e0 & 1) != 0) {
      _ZdlPv(local_1d0);
    }
    if ((uVar10 & 1) != 0) {
      while (uVar10 = FUN_0048795c(&local_1c8), (uVar10 & 1) != 0) {
        uVar10 = FUN_0048797c(&local_1c8,0);
                    /* try { // try from 008ebccc to 009ebcd3 has its CatchHandler @ 008ef2e8 */
        lVar11 = FUN_0048797c(&local_1c8,1);
        puVar3 = *(ulong **)(param_1 + 0x10);
                    /* try { // try from 008ebcd4 to 009ebd9b has its CatchHandler @ 008df140 */
        if (puVar3 < *(ulong **)(param_1 + 0x18)) {
          *puVar3 = uVar10 & 0xffffffff | lVar11 << 0x20;
          *(ulong **)(param_1 + 0x10) = puVar3 + 1;
        }
        else {
          __src = *(void **)pbVar14;
          lVar15 = (long)puVar3 - (long)__src >> 3;
          uVar1 = lVar15 + 1;
          if (uVar1 >> 0x3d != 0) {
            if (*(long *)(lVar4 + 0x28) == local_70) {
              FUN_008f8a40(pbVar14);
LAB_008ebe5c:
              if (*(long *)(lVar4 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                FUN_00440f00();
              }
            }
            goto LAB_008ebec4;
          }
          uVar12 = (long)*(ulong **)(param_1 + 0x18) - (long)__src;
          uVar13 = (long)uVar12 >> 2;
          if (uVar13 <= uVar1) {
            uVar13 = uVar1;
          }
          if (0x7ffffffffffffff7 < uVar12) {
            uVar13 = 0x1fffffffffffffff;
          }
          if (uVar13 == 0) {
            __dest = (void *)0x0;
          }
          else {
            if (uVar13 >> 0x3d != 0) goto LAB_008ebe5c;
            __dest = (void *)_Znwm(uVar13 << 3);
          }
          puVar2 = (ulong *)((long)__dest + lVar15 * 8);
          puVar16 = puVar2 + 1;
          *puVar2 = uVar10 & 0xffffffff | lVar11 << 0x20;
          memcpy(__dest,__src,(long)puVar3 - (long)__src);
          *(void **)(param_1 + 8) = __dest;
          *(ulong **)(param_1 + 0x10) = puVar16;
          *(void **)(param_1 + 0x18) = (void *)((long)__dest + uVar13 * 8);
          if (__src != (void *)0x0) {
            _ZdlPv(__src);
          }
          *(ulong **)(param_1 + 0x10) = puVar16;
        }
      }
      FUN_00488698(&local_1c8);
    }
    puVar9 = 
    PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88;
    local_180 = *(long *)
                 PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
    ;
    local_1c8 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
                    /* try { // try from 008ebd9c to 009ebe8b has its CatchHandler @ 008ef2e4 */
    *(undefined8 *)((long)&local_180 + *(long *)(local_180 + -0x18)) =
         *(undefined8 *)
          (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
          + 0x18);
    local_178[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                   + 0x10;
    if ((local_138 & 1) != 0) {
      _ZdlPv(local_128);
    }
    _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178);
    _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_180,puVar9 + 8);
    _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_110);
    if ((local_1a8 & 1) != 0) {
      _ZdlPv(local_198);
    }
    if (local_1c0 != (void *)0x0) {
      local_1b8 = local_1c0;
      _ZdlPv(local_1c0);
    }
  }
  if (*(long *)(lVar4 + 0x28) == local_70) {
    return;
  }
LAB_008ebec4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008ebbcc"></a> `008ebbcc` | `ff c3 07 d1` | sub sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-008ebbd0"></a> `008ebbd0` | `fd 7b 19 a9` | stp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-008ebbd4"></a> `008ebbd4` | `fc 6f 1a a9` | stp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-008ebbd8"></a> `008ebbd8` | `fa 67 1b a9` | stp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-008ebbdc"></a> `008ebbdc` | `f8 5f 1c a9` | stp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-008ebbe0"></a> `008ebbe0` | `f6 57 1d a9` | stp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-008ebbe4"></a> `008ebbe4` | `f4 4f 1e a9` | stp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-008ebbe8"></a> `008ebbe8` | `fd 43 06 91` | add x29,sp,#0x190 | `FALL_THROUGH`
<a id="insn-008ebbec"></a> `008ebbec` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008ebbf0"></a> `008ebbf0` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-008ebbf4"></a> `008ebbf4` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008ebbf8"></a> `008ebbf8` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-008ebbfc"></a> `008ebbfc` | `a8 10 00 37` | tbnz w8,#0x0,0x008ebe10 | `CONDITIONAL_JUMP`
<a id="insn-008ebc00"></a> `008ebc00` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-008ebc04"></a> `008ebc04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008ebc08"></a> `008ebc08` | `e9 07 00 f9` | str x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008ebc0c"></a> `008ebc0c` | `08 00 00 39` | strb w8,[x0] | `FALL_THROUGH`
<a id="insn-008ebc10"></a> `008ebc10` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebc14"></a> `008ebc14` | `93 70 ee 97` | bl 0x00487e60 | `UNCONDITIONAL_CALL`
<a id="insn-008ebc18"></a> `008ebc18` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-008ebc1c"></a> `008ebc1c` | `c9 1b 00 b0` | adrp x9,0xc64000 | `FALL_THROUGH`
<a id="insn-008ebc20"></a> `008ebc20` | `29 21 38 91` | add x9,x9,#0xe08 | `FALL_THROUGH`
<a id="insn-008ebc24"></a> `008ebc24` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-008ebc28"></a> `008ebc28` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008ebc2c"></a> `008ebc2c` | `88 06 00 f9` | str x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-008ebc30"></a> `008ebc30` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-008ebc34"></a> `008ebc34` | `cb b0 0d 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-008ebc38"></a> `008ebc38` | `ca cd ff b0` | adrp x10,0x2a4000 | `FALL_THROUGH`
<a id="insn-008ebc3c"></a> `008ebc3c` | `4a 89 27 91` | add x10,x10,#0x9e2 | `FALL_THROUGH`
<a id="insn-008ebc40"></a> `008ebc40` | `c8 ce ff 90` | adrp x8,0x2c3000 | `FALL_THROUGH`
<a id="insn-008ebc44"></a> `008ebc44` | `41 09 40 ad` | ldp q1,q2,[x10] | `FALL_THROUGH`
<a id="insn-008ebc48"></a> `008ebc48` | `00 b9 c0 3d` | ldr q0,[x8, #0x2e0] | `FALL_THROUGH`
<a id="insn-008ebc4c"></a> `008ebc4c` | `69 ce 8e 52` | mov w9,#0x7673 | `FALL_THROUGH`
<a id="insn-008ebc50"></a> `008ebc50` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ebc54"></a> `008ebc54` | `09 40 00 79` | strh w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-008ebc58"></a> `008ebc58` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ebc5c"></a> `008ebc5c` | `01 08 00 ad` | stp q1,q2,[x0] | `FALL_THROUGH`
<a id="insn-008ebc60"></a> `008ebc60` | `1f 88 00 39` | strb wzr,[x0, #0x22] | `FALL_THROUGH`
<a id="insn-008ebc64"></a> `008ebc64` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebc68"></a> `008ebc68` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008ebc6c"></a> `008ebc6c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008ebc70"></a> `008ebc70` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008ebc74"></a> `008ebc74` | `45 95 08 94` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-008ebc78"></a> `008ebc78` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ebc7c"></a> `008ebc7c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-008ebc80"></a> `008ebc80` | `68 00 00 36` | tbz w8,#0x0,0x008ebc8c | `CONDITIONAL_JUMP`
<a id="insn-008ebc84"></a> `008ebc84` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ebc88"></a> `008ebc88` | `be b0 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008ebc8c"></a> `008ebc8c` | `95 07 00 36` | tbz w21,#0x0,0x008ebd7c | `CONDITIONAL_JUMP`
<a id="insn-008ebc90"></a> `008ebc90` | `1c 00 fc 92` | mov x28,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-008ebc94"></a> `008ebc94` | `05 00 00 14` | b 0x008ebca8 | `UNCONDITIONAL_JUMP`
<a id="insn-008ebc98"></a> `008ebc98` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-008ebc9c"></a> `008ebc9c` | `08 81 17 aa` | orr x8,x8,x23, LSL #0x20 | `FALL_THROUGH`
<a id="insn-008ebca0"></a> `008ebca0` | `48 87 00 f8` | str x8,[x26], #0x8 | `FALL_THROUGH`
<a id="insn-008ebca4"></a> `008ebca4` | `7a 0a 00 f9` | str x26,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-008ebca8"></a> `008ebca8` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebcac"></a> `008ebcac` | `2c 6f ee 97` | bl 0x0048795c | `UNCONDITIONAL_CALL`
<a id="insn-008ebcb0"></a> `008ebcb0` | `20 06 00 36` | tbz w0,#0x0,0x008ebd74 | `CONDITIONAL_JUMP`
<a id="insn-008ebcb4"></a> `008ebcb4` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebcb8"></a> `008ebcb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-008ebcbc"></a> `008ebcbc` | `30 6f ee 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-008ebcc0"></a> `008ebcc0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-008ebcc4"></a> `008ebcc4` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebcc8"></a> `008ebcc8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-008ebccc"></a> `008ebccc` | `2c 6f ee 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-008ebcd0"></a> `008ebcd0` | `7a 22 41 a9` | ldp x26,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-008ebcd4"></a> `008ebcd4` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-008ebcd8"></a> `008ebcd8` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-008ebcdc"></a> `008ebcdc` | `e3 fd ff 54` | b.cc 0x008ebc98 | `CONDITIONAL_JUMP`
<a id="insn-008ebce0"></a> `008ebce0` | `96 02 40 f9` | ldr x22,[x20] | `FALL_THROUGH`
<a id="insn-008ebce4"></a> `008ebce4` | `58 03 16 cb` | sub x24,x26,x22 | `FALL_THROUGH`
<a id="insn-008ebce8"></a> `008ebce8` | `1a ff 43 93` | asr x26,x24,#0x3 | `FALL_THROUGH`
<a id="insn-008ebcec"></a> `008ebcec` | `49 07 00 91` | add x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-008ebcf0"></a> `008ebcf0` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-008ebcf4"></a> `008ebcf4` | `6a 0a 00 b5` | cbnz x10,0x008ebe40 | `CONDITIONAL_JUMP`
<a id="insn-008ebcf8"></a> `008ebcf8` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-008ebcfc"></a> `008ebcfc` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-008ebd00"></a> `008ebd00` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-008ebd04"></a> `008ebd04` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-008ebd08"></a> `008ebd08` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-008ebd0c"></a> `008ebd0c` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-008ebd10"></a> `008ebd10` | `3b 31 9c 9a` | csel x27,x9,x28,cc | `FALL_THROUGH`
<a id="insn-008ebd14"></a> `008ebd14` | `fb 00 00 b4` | cbz x27,0x008ebd30 | `CONDITIONAL_JUMP`
<a id="insn-008ebd18"></a> `008ebd18` | `68 ff 7d d3` | lsr x8,x27,#0x3d | `FALL_THROUGH`
<a id="insn-008ebd1c"></a> `008ebd1c` | `08 0a 00 b5` | cbnz x8,0x008ebe5c | `CONDITIONAL_JUMP`
<a id="insn-008ebd20"></a> `008ebd20` | `60 f3 7d d3` | lsl x0,x27,#0x3 | `FALL_THROUGH`
<a id="insn-008ebd24"></a> `008ebd24` | `8f b0 0d 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-008ebd28"></a> `008ebd28` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-008ebd2c"></a> `008ebd2c` | `02 00 00 14` | b 0x008ebd34 | `UNCONDITIONAL_JUMP`
<a id="insn-008ebd30"></a> `008ebd30` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-008ebd34"></a> `008ebd34` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-008ebd38"></a> `008ebd38` | `3a 0f 1a 8b` | add x26,x25,x26, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008ebd3c"></a> `008ebd3c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-008ebd40"></a> `008ebd40` | `08 81 17 aa` | orr x8,x8,x23, LSL #0x20 | `FALL_THROUGH`
<a id="insn-008ebd44"></a> `008ebd44` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-008ebd48"></a> `008ebd48` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-008ebd4c"></a> `008ebd4c` | `35 0f 1b 8b` | add x21,x25,x27, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008ebd50"></a> `008ebd50` | `48 87 00 f8` | str x8,[x26], #0x8 | `FALL_THROUGH`
<a id="insn-008ebd54"></a> `008ebd54` | `df b0 0d 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-008ebd58"></a> `008ebd58` | `79 ea 00 a9` | stp x25,x26,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008ebd5c"></a> `008ebd5c` | `75 0e 00 f9` | str x21,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-008ebd60"></a> `008ebd60` | `76 00 00 b4` | cbz x22,0x008ebd6c | `CONDITIONAL_JUMP`
<a id="insn-008ebd64"></a> `008ebd64` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008ebd68"></a> `008ebd68` | `86 b0 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008ebd6c"></a> `008ebd6c` | `7a 0a 00 f9` | str x26,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-008ebd70"></a> `008ebd70` | `ce ff ff 17` | b 0x008ebca8 | `UNCONDITIONAL_JUMP`
<a id="insn-008ebd74"></a> `008ebd74` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebd78"></a> `008ebd78` | `48 72 ee 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-008ebd7c"></a> `008ebd7c` | `68 1d 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-008ebd80"></a> `008ebd80` | `75 1d 00 f0` | adrp x21,0xc9a000 | `FALL_THROUGH`
<a id="insn-008ebd84"></a> `008ebd84` | `f4 a3 00 91` | add x20,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ebd88"></a> `008ebd88` | `08 41 46 f9` | ldr x8,[x8, #0xc80] | `FALL_THROUGH`
<a id="insn-008ebd8c"></a> `008ebd8c` | `b5 46 46 f9` | ldr x21,[x21, #0xc88] | `FALL_THROUGH`
<a id="insn-008ebd90"></a> `008ebd90` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-008ebd94"></a> `008ebd94` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-008ebd98"></a> `008ebd98` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-008ebd9c"></a> `008ebd9c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008ebda0"></a> `008ebda0` | `e9 3b 00 f9` | str x9,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008ebda4"></a> `008ebda4` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-008ebda8"></a> `008ebda8` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-008ebdac"></a> `008ebdac` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ebdb0"></a> `008ebdb0` | `68 1d 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-008ebdb4"></a> `008ebdb4` | `08 49 46 f9` | ldr x8,[x8, #0xc90] | `FALL_THROUGH`
<a id="insn-008ebdb8"></a> `008ebdb8` | `e9 e3 42 39` | ldrb w9,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-008ebdbc"></a> `008ebdbc` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-008ebdc0"></a> `008ebdc0` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-008ebdc4"></a> `008ebdc4` | `69 00 00 36` | tbz w9,#0x0,0x008ebdd0 | `CONDITIONAL_JUMP`
<a id="insn-008ebdc8"></a> `008ebdc8` | `e0 67 40 f9` | ldr x0,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-008ebdcc"></a> `008ebdcc` | `6d b0 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008ebdd0"></a> `008ebdd0` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-008ebdd4"></a> `008ebdd4` | `a7 b0 0d 94` | bl 0x00c58070 | `UNCONDITIONAL_CALL`
<a id="insn-008ebdd8"></a> `008ebdd8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-008ebddc"></a> `008ebddc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ebde0"></a> `008ebde0` | `a8 b0 0d 94` | bl 0x00c58080 | `UNCONDITIONAL_CALL`
<a id="insn-008ebde4"></a> `008ebde4` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-008ebde8"></a> `008ebde8` | `aa b0 0d 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-008ebdec"></a> `008ebdec` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-008ebdf0"></a> `008ebdf0` | `68 00 00 36` | tbz w8,#0x0,0x008ebdfc | `CONDITIONAL_JUMP`
<a id="insn-008ebdf4"></a> `008ebdf4` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-008ebdf8"></a> `008ebdf8` | `62 b0 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008ebdfc"></a> `008ebdfc` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008ebe00"></a> `008ebe00` | `60 00 00 b4` | cbz x0,0x008ebe0c | `CONDITIONAL_JUMP`
<a id="insn-008ebe04"></a> `008ebe04` | `e0 1f 00 f9` | str x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-008ebe08"></a> `008ebe08` | `5e b0 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008ebe0c"></a> `008ebe0c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008ebe10"></a> `008ebe10` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-008ebe14"></a> `008ebe14` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008ebe18"></a> `008ebe18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ebe1c"></a> `008ebe1c` | `41 05 00 54` | b.ne 0x008ebec4 | `CONDITIONAL_JUMP`
<a id="insn-008ebe20"></a> `008ebe20` | `f4 4f 5e a9` | ldp x20,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-008ebe24"></a> `008ebe24` | `f6 57 5d a9` | ldp x22,x21,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-008ebe28"></a> `008ebe28` | `f8 5f 5c a9` | ldp x24,x23,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-008ebe2c"></a> `008ebe2c` | `fa 67 5b a9` | ldp x26,x25,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-008ebe30"></a> `008ebe30` | `fc 6f 5a a9` | ldp x28,x27,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-008ebe34"></a> `008ebe34` | `fd 7b 59 a9` | ldp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-008ebe38"></a> `008ebe38` | `ff c3 07 91` | add sp,sp,#0x1f0 | `FALL_THROUGH`
<a id="insn-008ebe3c"></a> `008ebe3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008ebe40"></a> `008ebe40` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008ebe44"></a> `008ebe44` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-008ebe48"></a> `008ebe48` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008ebe4c"></a> `008ebe4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ebe50"></a> `008ebe50` | `a1 03 00 54` | b.ne 0x008ebec4 | `CONDITIONAL_JUMP`
<a id="insn-008ebe54"></a> `008ebe54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008ebe58"></a> `008ebe58` | `fa 32 00 94` | bl 0x008f8a40 | `UNCONDITIONAL_CALL`
<a id="insn-008ebe5c"></a> `008ebe5c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008ebe60"></a> `008ebe60` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-008ebe64"></a> `008ebe64` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008ebe68"></a> `008ebe68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ebe6c"></a> `008ebe6c` | `c1 02 00 54` | b.ne 0x008ebec4 | `CONDITIONAL_JUMP`
<a id="insn-008ebe70"></a> `008ebe70` | `24 54 ed 97` | bl 0x00440f00 | `CALL_TERMINATOR`
<a id="insn-008ebec4"></a> `008ebec4` | `3b b0 0d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008ebbcc`](#insn-008ebbcc) 範囲 `[['008ebbcc', '008ebbff']]`
  - `CONDITIONAL_JUMP` [`008ebbfc`](#insn-008ebbfc) → [`008ebe10`](#insn-008ebe10)
  - `FALL_THROUGH` [`008ebbfc`](#insn-008ebbfc) → [`008ebc00`](#insn-008ebc00)
- ブロック [`008ebc00`](#insn-008ebc00) 範囲 `[['008ebc00', '008ebc33']]`
  - `FALL_THROUGH` [`008ebc30`](#insn-008ebc30) → [`008ebc34`](#insn-008ebc34)
- ブロック [`008ebc34`](#insn-008ebc34) 範囲 `[['008ebc34', '008ebc83']]`
  - `CONDITIONAL_JUMP` [`008ebc80`](#insn-008ebc80) → [`008ebc8c`](#insn-008ebc8c)
  - `FALL_THROUGH` [`008ebc80`](#insn-008ebc80) → [`008ebc84`](#insn-008ebc84)
- ブロック [`008ebc84`](#insn-008ebc84) 範囲 `[['008ebc84', '008ebc8b']]`
  - `FALL_THROUGH` [`008ebc88`](#insn-008ebc88) → [`008ebc8c`](#insn-008ebc8c)
- ブロック [`008ebc8c`](#insn-008ebc8c) 範囲 `[['008ebc8c', '008ebc8f']]`
  - `CONDITIONAL_JUMP` [`008ebc8c`](#insn-008ebc8c) → [`008ebd7c`](#insn-008ebd7c)
  - `FALL_THROUGH` [`008ebc8c`](#insn-008ebc8c) → [`008ebc90`](#insn-008ebc90)
- ブロック [`008ebc90`](#insn-008ebc90) 範囲 `[['008ebc90', '008ebc97']]`
  - `UNCONDITIONAL_JUMP` [`008ebc94`](#insn-008ebc94) → [`008ebca8`](#insn-008ebca8)
- ブロック [`008ebc98`](#insn-008ebc98) 範囲 `[['008ebc98', '008ebca7']]`
  - `FALL_THROUGH` [`008ebca4`](#insn-008ebca4) → [`008ebca8`](#insn-008ebca8)
- ブロック [`008ebca8`](#insn-008ebca8) 範囲 `[['008ebca8', '008ebcb3']]`
  - `CONDITIONAL_JUMP` [`008ebcb0`](#insn-008ebcb0) → [`008ebd74`](#insn-008ebd74)
  - `FALL_THROUGH` [`008ebcb0`](#insn-008ebcb0) → [`008ebcb4`](#insn-008ebcb4)
- ブロック [`008ebcb4`](#insn-008ebcb4) 範囲 `[['008ebcb4', '008ebccb']]`
  - `FALL_THROUGH` [`008ebcc8`](#insn-008ebcc8) → [`008ebccc`](#insn-008ebccc)
- ブロック [`008ebccc`](#insn-008ebccc) 範囲 `[['008ebccc', '008ebcd3']]`
  - `FALL_THROUGH` [`008ebcd0`](#insn-008ebcd0) → [`008ebcd4`](#insn-008ebcd4)
- ブロック [`008ebcd4`](#insn-008ebcd4) 範囲 `[['008ebcd4', '008ebcdf']]`
  - `CONDITIONAL_JUMP` [`008ebcdc`](#insn-008ebcdc) → [`008ebc98`](#insn-008ebc98)
  - `FALL_THROUGH` [`008ebcdc`](#insn-008ebcdc) → [`008ebce0`](#insn-008ebce0)
- ブロック [`008ebce0`](#insn-008ebce0) 範囲 `[['008ebce0', '008ebcf7']]`
  - `CONDITIONAL_JUMP` [`008ebcf4`](#insn-008ebcf4) → [`008ebe40`](#insn-008ebe40)
  - `FALL_THROUGH` [`008ebcf4`](#insn-008ebcf4) → [`008ebcf8`](#insn-008ebcf8)
- ブロック [`008ebcf8`](#insn-008ebcf8) 範囲 `[['008ebcf8', '008ebd17']]`
  - `CONDITIONAL_JUMP` [`008ebd14`](#insn-008ebd14) → [`008ebd30`](#insn-008ebd30)
  - `FALL_THROUGH` [`008ebd14`](#insn-008ebd14) → [`008ebd18`](#insn-008ebd18)
- ブロック [`008ebd18`](#insn-008ebd18) 範囲 `[['008ebd18', '008ebd1f']]`
  - `CONDITIONAL_JUMP` [`008ebd1c`](#insn-008ebd1c) → [`008ebe5c`](#insn-008ebe5c)
  - `FALL_THROUGH` [`008ebd1c`](#insn-008ebd1c) → [`008ebd20`](#insn-008ebd20)
- ブロック [`008ebd20`](#insn-008ebd20) 範囲 `[['008ebd20', '008ebd2f']]`
  - `UNCONDITIONAL_JUMP` [`008ebd2c`](#insn-008ebd2c) → [`008ebd34`](#insn-008ebd34)
- ブロック [`008ebd30`](#insn-008ebd30) 範囲 `[['008ebd30', '008ebd33']]`
  - `FALL_THROUGH` [`008ebd30`](#insn-008ebd30) → [`008ebd34`](#insn-008ebd34)
- ブロック [`008ebd34`](#insn-008ebd34) 範囲 `[['008ebd34', '008ebd63']]`
  - `CONDITIONAL_JUMP` [`008ebd60`](#insn-008ebd60) → [`008ebd6c`](#insn-008ebd6c)
  - `FALL_THROUGH` [`008ebd60`](#insn-008ebd60) → [`008ebd64`](#insn-008ebd64)
- ブロック [`008ebd64`](#insn-008ebd64) 範囲 `[['008ebd64', '008ebd6b']]`
  - `FALL_THROUGH` [`008ebd68`](#insn-008ebd68) → [`008ebd6c`](#insn-008ebd6c)
- ブロック [`008ebd6c`](#insn-008ebd6c) 範囲 `[['008ebd6c', '008ebd73']]`
  - `UNCONDITIONAL_JUMP` [`008ebd70`](#insn-008ebd70) → [`008ebca8`](#insn-008ebca8)
- ブロック [`008ebd74`](#insn-008ebd74) 範囲 `[['008ebd74', '008ebd7b']]`
  - `FALL_THROUGH` [`008ebd78`](#insn-008ebd78) → [`008ebd7c`](#insn-008ebd7c)
- ブロック [`008ebd7c`](#insn-008ebd7c) 範囲 `[['008ebd7c', '008ebd9b']]`
  - `FALL_THROUGH` [`008ebd98`](#insn-008ebd98) → [`008ebd9c`](#insn-008ebd9c)
- ブロック [`008ebd9c`](#insn-008ebd9c) 範囲 `[['008ebd9c', '008ebdc7']]`
  - `CONDITIONAL_JUMP` [`008ebdc4`](#insn-008ebdc4) → [`008ebdd0`](#insn-008ebdd0)
  - `FALL_THROUGH` [`008ebdc4`](#insn-008ebdc4) → [`008ebdc8`](#insn-008ebdc8)
- ブロック [`008ebdc8`](#insn-008ebdc8) 範囲 `[['008ebdc8', '008ebdcf']]`
  - `FALL_THROUGH` [`008ebdcc`](#insn-008ebdcc) → [`008ebdd0`](#insn-008ebdd0)
- ブロック [`008ebdd0`](#insn-008ebdd0) 範囲 `[['008ebdd0', '008ebdf3']]`
  - `CONDITIONAL_JUMP` [`008ebdf0`](#insn-008ebdf0) → [`008ebdfc`](#insn-008ebdfc)
  - `FALL_THROUGH` [`008ebdf0`](#insn-008ebdf0) → [`008ebdf4`](#insn-008ebdf4)
- ブロック [`008ebdf4`](#insn-008ebdf4) 範囲 `[['008ebdf4', '008ebdfb']]`
  - `FALL_THROUGH` [`008ebdf8`](#insn-008ebdf8) → [`008ebdfc`](#insn-008ebdfc)
- ブロック [`008ebdfc`](#insn-008ebdfc) 範囲 `[['008ebdfc', '008ebe03']]`
  - `CONDITIONAL_JUMP` [`008ebe00`](#insn-008ebe00) → [`008ebe0c`](#insn-008ebe0c)
  - `FALL_THROUGH` [`008ebe00`](#insn-008ebe00) → [`008ebe04`](#insn-008ebe04)
- ブロック [`008ebe04`](#insn-008ebe04) 範囲 `[['008ebe04', '008ebe0b']]`
  - `FALL_THROUGH` [`008ebe08`](#insn-008ebe08) → [`008ebe0c`](#insn-008ebe0c)
- ブロック [`008ebe0c`](#insn-008ebe0c) 範囲 `[['008ebe0c', '008ebe0f']]`
  - `FALL_THROUGH` [`008ebe0c`](#insn-008ebe0c) → [`008ebe10`](#insn-008ebe10)
- ブロック [`008ebe10`](#insn-008ebe10) 範囲 `[['008ebe10', '008ebe1f']]`
  - `CONDITIONAL_JUMP` [`008ebe1c`](#insn-008ebe1c) → [`008ebec4`](#insn-008ebec4)
  - `FALL_THROUGH` [`008ebe1c`](#insn-008ebe1c) → [`008ebe20`](#insn-008ebe20)
- ブロック [`008ebe20`](#insn-008ebe20) 範囲 `[['008ebe20', '008ebe3f']]`
- ブロック [`008ebe40`](#insn-008ebe40) 範囲 `[['008ebe40', '008ebe53']]`
  - `CONDITIONAL_JUMP` [`008ebe50`](#insn-008ebe50) → [`008ebec4`](#insn-008ebec4)
  - `FALL_THROUGH` [`008ebe50`](#insn-008ebe50) → [`008ebe54`](#insn-008ebe54)
- ブロック [`008ebe54`](#insn-008ebe54) 範囲 `[['008ebe54', '008ebe5b']]`
  - `FALL_THROUGH` [`008ebe58`](#insn-008ebe58) → [`008ebe5c`](#insn-008ebe5c)
- ブロック [`008ebe5c`](#insn-008ebe5c) 範囲 `[['008ebe5c', '008ebe6f']]`
  - `CONDITIONAL_JUMP` [`008ebe6c`](#insn-008ebe6c) → [`008ebec4`](#insn-008ebec4)
  - `FALL_THROUGH` [`008ebe6c`](#insn-008ebe6c) → [`008ebe70`](#insn-008ebe70)
- ブロック [`008ebe70`](#insn-008ebe70) 範囲 `[['008ebe70', '008ebe73']]`
- ブロック [`008ebec4`](#insn-008ebec4) 範囲 `[['008ebec4', '008ebec7']]`

## 命令位置別の参照

- [`008ebbd0`](#insn-008ebbd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbd4`](#insn-008ebbd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbd8`](#insn-008ebbd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbdc`](#insn-008ebbdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbe0`](#insn-008ebbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbe4`](#insn-008ebbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbf4`](#insn-008ebbf4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebbfc`](#insn-008ebbfc) → [`008ebe10`](#insn-008ebe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc08`](#insn-008ebc08) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc14`](#insn-008ebc14) → [`00487e60`](../00487/00487e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e60` · 推定シンボル `None` · 推定型 `None`
- [`008ebc28`](#insn-008ebc28) → `00c64e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008ebc28`](#insn-008ebc28) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc34`](#insn-008ebc34) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`008ebc44`](#insn-008ebc44) → `002a49e2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ebc44`](#insn-008ebc44) → `002a49f2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ebc48`](#insn-008ebc48) → `002c32e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc50`](#insn-008ebc50) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc58`](#insn-008ebc58) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc74`](#insn-008ebc74) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`008ebc78`](#insn-008ebc78) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc80`](#insn-008ebc80) → [`008ebc8c`](#insn-008ebc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc84`](#insn-008ebc84) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc88`](#insn-008ebc88) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008ebc8c`](#insn-008ebc8c) → [`008ebd7c`](#insn-008ebd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebc94`](#insn-008ebc94) → [`008ebca8`](#insn-008ebca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebcac`](#insn-008ebcac) → [`0048795c`](../00487/0048795c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048795c` · 推定シンボル `None` · 推定型 `None`
- [`008ebcb0`](#insn-008ebcb0) → [`008ebd74`](#insn-008ebd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebcbc`](#insn-008ebcbc) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`008ebccc`](#insn-008ebccc) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`008ebcdc`](#insn-008ebcdc) → [`008ebc98`](#insn-008ebc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebcf4`](#insn-008ebcf4) → [`008ebe40`](#insn-008ebe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd14`](#insn-008ebd14) → [`008ebd30`](#insn-008ebd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd1c`](#insn-008ebd1c) → [`008ebe5c`](#insn-008ebe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd24`](#insn-008ebd24) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`008ebd2c`](#insn-008ebd2c) → [`008ebd34`](#insn-008ebd34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd54`](#insn-008ebd54) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`008ebd60`](#insn-008ebd60) → [`008ebd6c`](#insn-008ebd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd68`](#insn-008ebd68) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008ebd70`](#insn-008ebd70) → [`008ebca8`](#insn-008ebca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebd78`](#insn-008ebd78) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`008ebd88`](#insn-008ebd88) → `00c9ac80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008ebd8c`](#insn-008ebd8c) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008ebd94`](#insn-008ebd94) → `00c932d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`008ebd9c`](#insn-008ebd9c) → `00c658e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008ebd9c`](#insn-008ebd9c) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebda0`](#insn-008ebda0) → `00c910e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008ebda0`](#insn-008ebda0) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebda4`](#insn-008ebda4) → `00c910c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`008ebda8`](#insn-008ebda8) → `00c932e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`008ebdac`](#insn-008ebdac) → `00c91108`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008ebdb4`](#insn-008ebdb4) → `00c9ac90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008ebdb8`](#insn-008ebdb8) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdc0`](#insn-008ebdc0) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`008ebdc0`](#insn-008ebdc0) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdc4`](#insn-008ebdc4) → [`008ebdd0`](#insn-008ebdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdc8`](#insn-008ebdc8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdcc`](#insn-008ebdcc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008ebdd4`](#insn-008ebdd4) → [`00c58070`](../00c58/00c58070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58070` · 推定シンボル `None` · 推定型 `None`
- [`008ebdd8`](#insn-008ebdd8) → `00c932d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`008ebde0`](#insn-008ebde0) → [`00c58080`](../00c58/00c58080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58080` · 推定シンボル `None` · 推定型 `None`
- [`008ebde8`](#insn-008ebde8) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`008ebdec`](#insn-008ebdec) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdf0`](#insn-008ebdf0) → [`008ebdfc`](#insn-008ebdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdf4`](#insn-008ebdf4) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebdf8`](#insn-008ebdf8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008ebdfc`](#insn-008ebdfc) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe00`](#insn-008ebe00) → [`008ebe0c`](#insn-008ebe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe04`](#insn-008ebe04) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe08`](#insn-008ebe08) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008ebe0c`](#insn-008ebe0c) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe14`](#insn-008ebe14) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe1c`](#insn-008ebe1c) → [`008ebec4`](#insn-008ebec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe20`](#insn-008ebe20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe24`](#insn-008ebe24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe28`](#insn-008ebe28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe2c`](#insn-008ebe2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe30`](#insn-008ebe30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe34`](#insn-008ebe34) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe40`](#insn-008ebe40) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe48`](#insn-008ebe48) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe50`](#insn-008ebe50) → [`008ebec4`](#insn-008ebec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe58`](#insn-008ebe58) → [`008f8a40`](../008f8/008f8a40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008f8a40` · 推定シンボル `None` · 推定型 `None`
- [`008ebe5c`](#insn-008ebe5c) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe64`](#insn-008ebe64) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe6c`](#insn-008ebe6c) → [`008ebec4`](#insn-008ebec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ebe70`](#insn-008ebe70) → [`00440f00`](../00440/00440f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440f00` · 推定シンボル `None` · 推定型 `None`
- [`008ebec4`](#insn-008ebec4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008ebbd0`](#insn-008ebbd0)

~~~json
{
  "source": "008ebbd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbd4`](#insn-008ebbd4)

~~~json
{
  "source": "008ebbd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbd8`](#insn-008ebbd8)

~~~json
{
  "source": "008ebbd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbdc`](#insn-008ebbdc)

~~~json
{
  "source": "008ebbdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbe0`](#insn-008ebbe0)

~~~json
{
  "source": "008ebbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbe4`](#insn-008ebbe4)

~~~json
{
  "source": "008ebbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbf4`](#insn-008ebbf4)

~~~json
{
  "source": "008ebbf4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebbfc`](#insn-008ebbfc)

~~~json
{
  "source": "008ebbfc",
  "target": "008ebe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc08`](#insn-008ebc08)

~~~json
{
  "source": "008ebc08",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc14`](#insn-008ebc14)

~~~json
{
  "source": "008ebc14",
  "target": "00487e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebc28`](#insn-008ebc28)

~~~json
{
  "source": "008ebc28",
  "target": "00c64e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64e08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebc28`](#insn-008ebc28)

~~~json
{
  "source": "008ebc28",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc34`](#insn-008ebc34)

~~~json
{
  "source": "008ebc34",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebc44`](#insn-008ebc44)

~~~json
{
  "source": "008ebc44",
  "target": "002a49e2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a49e2",
  "offset": 0,
  "size": 35,
  "datatype": "string",
  "bytes": "6e79616e6b6f50696374757265426f6f6b446174615f43686172614765742e63",
  "capture_start": "002a49e2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`008ebc44`](#insn-008ebc44)

~~~json
{
  "source": "008ebc44",
  "target": "002a49f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a49e2",
  "offset": 16,
  "size": 35,
  "datatype": "string",
  "bytes": "6e79616e6b6f50696374757265426f6f6b446174615f43686172614765742e63",
  "capture_start": "002a49e2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`008ebc48`](#insn-008ebc48)

~~~json
{
  "source": "008ebc48",
  "target": "002c32e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc50`](#insn-008ebc50)

~~~json
{
  "source": "008ebc50",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc58`](#insn-008ebc58)

~~~json
{
  "source": "008ebc58",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc74`](#insn-008ebc74)

~~~json
{
  "source": "008ebc74",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebc78`](#insn-008ebc78)

~~~json
{
  "source": "008ebc78",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc80`](#insn-008ebc80)

~~~json
{
  "source": "008ebc80",
  "target": "008ebc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc84`](#insn-008ebc84)

~~~json
{
  "source": "008ebc84",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc88`](#insn-008ebc88)

~~~json
{
  "source": "008ebc88",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebc8c`](#insn-008ebc8c)

~~~json
{
  "source": "008ebc8c",
  "target": "008ebd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebc94`](#insn-008ebc94)

~~~json
{
  "source": "008ebc94",
  "target": "008ebca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebcac`](#insn-008ebcac)

~~~json
{
  "source": "008ebcac",
  "target": "0048795c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebcb0`](#insn-008ebcb0)

~~~json
{
  "source": "008ebcb0",
  "target": "008ebd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebcbc`](#insn-008ebcbc)

~~~json
{
  "source": "008ebcbc",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebccc`](#insn-008ebccc)

~~~json
{
  "source": "008ebccc",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebcdc`](#insn-008ebcdc)

~~~json
{
  "source": "008ebcdc",
  "target": "008ebc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebcf4`](#insn-008ebcf4)

~~~json
{
  "source": "008ebcf4",
  "target": "008ebe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd14`](#insn-008ebd14)

~~~json
{
  "source": "008ebd14",
  "target": "008ebd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd1c`](#insn-008ebd1c)

~~~json
{
  "source": "008ebd1c",
  "target": "008ebe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd24`](#insn-008ebd24)

~~~json
{
  "source": "008ebd24",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebd2c`](#insn-008ebd2c)

~~~json
{
  "source": "008ebd2c",
  "target": "008ebd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd54`](#insn-008ebd54)

~~~json
{
  "source": "008ebd54",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebd60`](#insn-008ebd60)

~~~json
{
  "source": "008ebd60",
  "target": "008ebd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd68`](#insn-008ebd68)

~~~json
{
  "source": "008ebd68",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebd70`](#insn-008ebd70)

~~~json
{
  "source": "008ebd70",
  "target": "008ebca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebd78`](#insn-008ebd78)

~~~json
{
  "source": "008ebd78",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebd88`](#insn-008ebd88)

~~~json
{
  "source": "008ebd88",
  "target": "00c9ac80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebd8c`](#insn-008ebd8c)

~~~json
{
  "source": "008ebd8c",
  "target": "00c9ac88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebd94`](#insn-008ebd94)

~~~json
{
  "source": "008ebd94",
  "target": "00c932d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebd9c`](#insn-008ebd9c)

~~~json
{
  "source": "008ebd9c",
  "target": "00c658e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c658e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebd9c`](#insn-008ebd9c)

~~~json
{
  "source": "008ebd9c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebda0`](#insn-008ebda0)

~~~json
{
  "source": "008ebda0",
  "target": "00c910e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebda0`](#insn-008ebda0)

~~~json
{
  "source": "008ebda0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebda4`](#insn-008ebda4)

~~~json
{
  "source": "008ebda4",
  "target": "00c910c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c910c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ebda8`](#insn-008ebda8)

~~~json
{
  "source": "008ebda8",
  "target": "00c932e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebdac`](#insn-008ebdac)

~~~json
{
  "source": "008ebdac",
  "target": "00c91108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91108",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebdb4`](#insn-008ebdb4)

~~~json
{
  "source": "008ebdb4",
  "target": "00c9ac90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebdb8`](#insn-008ebdb8)

~~~json
{
  "source": "008ebdb8",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdc0`](#insn-008ebdc0)

~~~json
{
  "source": "008ebdc0",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`008ebdc0`](#insn-008ebdc0)

~~~json
{
  "source": "008ebdc0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdc4`](#insn-008ebdc4)

~~~json
{
  "source": "008ebdc4",
  "target": "008ebdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdc8`](#insn-008ebdc8)

~~~json
{
  "source": "008ebdc8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdcc`](#insn-008ebdcc)

~~~json
{
  "source": "008ebdcc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebdd4`](#insn-008ebdd4)

~~~json
{
  "source": "008ebdd4",
  "target": "00c58070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebdd8`](#insn-008ebdd8)

~~~json
{
  "source": "008ebdd8",
  "target": "00c932d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008ebde0`](#insn-008ebde0)

~~~json
{
  "source": "008ebde0",
  "target": "00c58080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebde8`](#insn-008ebde8)

~~~json
{
  "source": "008ebde8",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebdec`](#insn-008ebdec)

~~~json
{
  "source": "008ebdec",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdf0`](#insn-008ebdf0)

~~~json
{
  "source": "008ebdf0",
  "target": "008ebdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdf4`](#insn-008ebdf4)

~~~json
{
  "source": "008ebdf4",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebdf8`](#insn-008ebdf8)

~~~json
{
  "source": "008ebdf8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebdfc`](#insn-008ebdfc)

~~~json
{
  "source": "008ebdfc",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe00`](#insn-008ebe00)

~~~json
{
  "source": "008ebe00",
  "target": "008ebe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe04`](#insn-008ebe04)

~~~json
{
  "source": "008ebe04",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe08`](#insn-008ebe08)

~~~json
{
  "source": "008ebe08",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebe0c`](#insn-008ebe0c)

~~~json
{
  "source": "008ebe0c",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe14`](#insn-008ebe14)

~~~json
{
  "source": "008ebe14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe1c`](#insn-008ebe1c)

~~~json
{
  "source": "008ebe1c",
  "target": "008ebec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe20`](#insn-008ebe20)

~~~json
{
  "source": "008ebe20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe24`](#insn-008ebe24)

~~~json
{
  "source": "008ebe24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe28`](#insn-008ebe28)

~~~json
{
  "source": "008ebe28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe2c`](#insn-008ebe2c)

~~~json
{
  "source": "008ebe2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe30`](#insn-008ebe30)

~~~json
{
  "source": "008ebe30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe34`](#insn-008ebe34)

~~~json
{
  "source": "008ebe34",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe40`](#insn-008ebe40)

~~~json
{
  "source": "008ebe40",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe48`](#insn-008ebe48)

~~~json
{
  "source": "008ebe48",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe50`](#insn-008ebe50)

~~~json
{
  "source": "008ebe50",
  "target": "008ebec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe58`](#insn-008ebe58)

~~~json
{
  "source": "008ebe58",
  "target": "008f8a40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebe5c`](#insn-008ebe5c)

~~~json
{
  "source": "008ebe5c",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe64`](#insn-008ebe64)

~~~json
{
  "source": "008ebe64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe6c`](#insn-008ebe6c)

~~~json
{
  "source": "008ebe6c",
  "target": "008ebec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ebe70`](#insn-008ebe70)

~~~json
{
  "source": "008ebe70",
  "target": "00440f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ebec4`](#insn-008ebec4)

~~~json
{
  "source": "008ebec4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
