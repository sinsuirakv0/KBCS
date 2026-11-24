# 004eadcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004c7f34`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0009.md#compare-0adde386999c036893ecd6ce59f00f7a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004eae0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eae0c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-ed37c0d77398070e4ec22bc641ff9bdd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eadcc",
  "name": "_ZNK5Botan11Private_Key19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESB_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "853204dc3ae7c35150113bd583f13b28bedab25be2939238eab8756ba7da3fac",
  "source_text_sha256": "853204dc3ae7c35150113bd583f13b28bedab25be2939238eab8756ba7da3fac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004eadcc",
        "004eaec3"
      ],
      [
        "004eaf54",
        "004eaf57"
      ]
    ],
    "bytes_sha256": "96345da8b677973cf516cbe672df22feb2dd07935017944d0806b70b5f9780c5",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c57b70](../00c57/00c57b70.md)

## 関連文字列（未確認候補）

~~~text
" does not support signatures"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2242 bytes

~~~c

void _ZNK5Botan11Private_Key19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESB_
               (long *param_1)

{
  long lVar1;
  long lVar2;
  undefined4 uVar3;
  byte bVar4;
  long lVar5;
  undefined *puVar6;
  long *plVar7;
  byte *pbVar8;
  undefined1 auStack_68 [24];
  undefined4 local_50;
  undefined3 uStack_4c;
  long local_48;
  
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  plVar7 = (long *)__cxa_allocate_exception(0x20);
  (**(code **)(*(long *)((long)param_1 + *(long *)(*param_1 + -0x80)) + 0x10))
            (auStack_68,(long)param_1 + *(long *)(*param_1 + -0x80));
  pbVar8 = (byte *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                             (auStack_68," does not support signatures");
  uVar3 = *(undefined4 *)(pbVar8 + 4);
  lVar1 = *(long *)(pbVar8 + 8);
  lVar2 = *(long *)(pbVar8 + 0x10);
  pbVar8[0x10] = 0;
  puVar6 = PTR__ZTVN5Botan9ExceptionE_00c9a9d0;
  pbVar8[0x11] = 0;
  pbVar8[0x12] = 0;
  pbVar8[0x13] = 0;
  pbVar8[0x14] = 0;
  pbVar8[0x15] = 0;
  pbVar8[0x16] = 0;
  pbVar8[0x17] = 0;
  local_50._0_3_ = (undefined3)*(undefined4 *)(pbVar8 + 1);
  local_50._3_1_ = (undefined1)uVar3;
  uStack_4c = (undefined3)((uint)uVar3 >> 8);
  bVar4 = *pbVar8;
  pbVar8[0] = 0;
  pbVar8[1] = 0;
  pbVar8[2] = 0;
  pbVar8[3] = 0;
  pbVar8[4] = 0;
  pbVar8[5] = 0;
  pbVar8[6] = 0;
  pbVar8[7] = 0;
  pbVar8[8] = 0;
  pbVar8[9] = 0;
  pbVar8[10] = 0;
  pbVar8[0xb] = 0;
  pbVar8[0xc] = 0;
  pbVar8[0xd] = 0;
  pbVar8[0xe] = 0;
  pbVar8[0xf] = 0;
  *plVar7 = (long)(puVar6 + 0x10);
  if ((bVar4 & 1) == 0) {
    *(byte *)(plVar7 + 1) = bVar4;
    plVar7[2] = lVar1;
    plVar7[3] = lVar2;
    *(undefined4 *)((long)plVar7 + 9) = local_50;
    *(undefined4 *)((long)plVar7 + 0xc) = uVar3;
  }
  else {
    FUN_0043bae0(plVar7 + 1,lVar2);
  }
  *plVar7 = (long)(PTR__ZTVN5Botan12Lookup_ErrorE_00c9abf0 + 0x10);
  if (*(long *)(lVar5 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
    __cxa_throw(plVar7,PTR__ZTIN5Botan12Lookup_ErrorE_00c9aa28,FUN_00535828);
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004eadcc"></a> `004eadcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004eadd0"></a> `004eadd0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004eadd4"></a> `004eadd4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004eadd8"></a> `004eadd8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004eaddc"></a> `004eaddc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004eade0"></a> `004eade0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004eade4"></a> `004eade4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004eade8"></a> `004eade8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004eadec"></a> `004eadec` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004eadf0"></a> `004eadf0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004eadf4"></a> `004eadf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eadf8"></a> `004eadf8` | `3e b3 1d 94` | bl 0x00c57af0 | `UNCONDITIONAL_CALL`
<a id="insn-004eadfc"></a> `004eadfc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004eae00"></a> `004eae00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004eae04"></a> `004eae04` | `09 01 58 f8` | ldur x9,[x8, #-0x80] | `FALL_THROUGH`
<a id="insn-004eae08"></a> `004eae08` | `88 6a 69 f8` | ldr x8,[x20, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004eae0c"></a> `004eae0c` | `0a 09 40 f9` | ldr x10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-004eae10"></a> `004eae10` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004eae14"></a> `004eae14` | `80 02 09 8b` | add x0,x20,x9 | `FALL_THROUGH`
<a id="insn-004eae18"></a> `004eae18` | `40 01 3f d6` | blr x10 | `COMPUTED_CALL`
<a id="insn-004eae1c"></a> `004eae1c` | `61 ee ff d0` | adrp x1,0x2b8000 | `FALL_THROUGH`
<a id="insn-004eae20"></a> `004eae20` | `21 20 07 91` | add x1,x1,#0x1c8 | `FALL_THROUGH`
<a id="insn-004eae24"></a> `004eae24` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004eae28"></a> `004eae28` | `52 b3 1d 94` | bl 0x00c57b70 | `UNCONDITIONAL_CALL`
<a id="insn-004eae2c"></a> `004eae2c` | `08 10 40 b8` | ldur w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-004eae30"></a> `004eae30` | `09 04 40 b9` | ldr w9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-004eae34"></a> `004eae34` | `02 d4 40 a9` | ldp x2,x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004eae38"></a> `004eae38` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004eae3c"></a> `004eae3c` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004eae40"></a> `004eae40` | `88 3d 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004eae44"></a> `004eae44` | `a9 33 1f b8` | stur w9,[x29, #-0xd] | `FALL_THROUGH`
<a id="insn-004eae48"></a> `004eae48` | `08 e9 44 f9` | ldr x8,[x8, #0x9d0] | `FALL_THROUGH`
<a id="insn-004eae4c"></a> `004eae4c` | `17 00 40 39` | ldrb w23,[x0] | `FALL_THROUGH`
<a id="insn-004eae50"></a> `004eae50` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-004eae54"></a> `004eae54` | `09 41 00 91` | add x9,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004eae58"></a> `004eae58` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004eae5c"></a> `004eae5c` | `09 85 00 f8` | str x9,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004eae60"></a> `004eae60` | `17 01 00 37` | tbnz w23,#0x0,0x004eae80 | `CONDITIONAL_JUMP`
<a id="insn-004eae64"></a> `004eae64` | `a8 03 5f b8` | ldur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004eae68"></a> `004eae68` | `a9 33 5f b8` | ldur w9,[x29, #-0xd] | `FALL_THROUGH`
<a id="insn-004eae6c"></a> `004eae6c` | `77 22 00 39` | strb w23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004eae70"></a> `004eae70` | `62 56 01 a9` | stp x2,x21,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004eae74"></a> `004eae74` | `68 92 00 b8` | stur w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-004eae78"></a> `004eae78` | `69 0e 00 b9` | str w9,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-004eae7c"></a> `004eae7c` | `04 00 00 14` | b 0x004eae8c | `UNCONDITIONAL_JUMP`
<a id="insn-004eae80"></a> `004eae80` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004eae84"></a> `004eae84` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004eae88"></a> `004eae88` | `16 43 fd 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004eae8c"></a> `004eae8c` | `88 3d 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004eae90"></a> `004eae90` | `08 f9 45 f9` | ldr x8,[x8, #0xbf0] | `FALL_THROUGH`
<a id="insn-004eae94"></a> `004eae94` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004eae98"></a> `004eae98` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004eae9c"></a> `004eae9c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004eaea0"></a> `004eaea0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eaea4"></a> `004eaea4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004eaea8"></a> `004eaea8` | `61 05 00 54` | b.ne 0x004eaf54 | `CONDITIONAL_JUMP`
<a id="insn-004eaeac"></a> `004eaeac` | `81 3d 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004eaeb0"></a> `004eaeb0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004eaeb4"></a> `004eaeb4` | `a2 4b 25 10` | adr x2,0x535828 | `FALL_THROUGH`
<a id="insn-004eaeb8"></a> `004eaeb8` | `21 14 45 f9` | ldr x1,[x1, #0xa28] | `FALL_THROUGH`
<a id="insn-004eaebc"></a> `004eaebc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004eaec0"></a> `004eaec0` | `14 b3 1d 94` | bl 0x00c57b10 | `CALL_TERMINATOR`
<a id="insn-004eaf54"></a> `004eaf54` | `e3 b2 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004eadcc`](#insn-004eadcc) 範囲 `[['004eadcc', '004eae63']]`
  - `CONDITIONAL_JUMP` [`004eae60`](#insn-004eae60) → [`004eae80`](#insn-004eae80)
  - `FALL_THROUGH` [`004eae60`](#insn-004eae60) → [`004eae64`](#insn-004eae64)
- ブロック [`004eae64`](#insn-004eae64) 範囲 `[['004eae64', '004eae7f']]`
  - `UNCONDITIONAL_JUMP` [`004eae7c`](#insn-004eae7c) → [`004eae8c`](#insn-004eae8c)
- ブロック [`004eae80`](#insn-004eae80) 範囲 `[['004eae80', '004eae8b']]`
  - `FALL_THROUGH` [`004eae88`](#insn-004eae88) → [`004eae8c`](#insn-004eae8c)
- ブロック [`004eae8c`](#insn-004eae8c) 範囲 `[['004eae8c', '004eaeab']]`
  - `CONDITIONAL_JUMP` [`004eaea8`](#insn-004eaea8) → [`004eaf54`](#insn-004eaf54)
  - `FALL_THROUGH` [`004eaea8`](#insn-004eaea8) → [`004eaeac`](#insn-004eaeac)
- ブロック [`004eaeac`](#insn-004eaeac) 範囲 `[['004eaeac', '004eaec3']]`
- ブロック [`004eaf54`](#insn-004eaf54) 範囲 `[['004eaf54', '004eaf57']]`

## 命令位置別の参照

- [`004eadd0`](#insn-004eadd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eadd4`](#insn-004eadd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eadd8`](#insn-004eadd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eaddc`](#insn-004eaddc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eadf4`](#insn-004eadf4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eadf8`](#insn-004eadf8) → [`00c57af0`](../00c57/00c57af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57af0` · 推定シンボル `None` · 推定型 `None`
- [`004eae20`](#insn-004eae20) → `002b81c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004eae28`](#insn-004eae28) → [`00c57b70`](../00c57/00c57b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b70` · 推定シンボル `None` · 推定型 `None`
- [`004eae3c`](#insn-004eae3c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae44`](#insn-004eae44) → `Stack[-0x4d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae48`](#insn-004eae48) → `00c9a9d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004eae5c`](#insn-004eae5c) → `00c67028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004eae60`](#insn-004eae60) → [`004eae80`](#insn-004eae80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae64`](#insn-004eae64) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae68`](#insn-004eae68) → `Stack[-0x4d]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae7c`](#insn-004eae7c) → [`004eae8c`](#insn-004eae8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eae88`](#insn-004eae88) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004eae90`](#insn-004eae90) → `00c9abf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004eae98`](#insn-004eae98) → `00c67078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004eaea0`](#insn-004eaea0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eaea8`](#insn-004eaea8) → [`004eaf54`](#insn-004eaf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eaeb4`](#insn-004eaeb4) → [`00535828`](../00535/00535828.md) · `PARAM` · `ANALYSIS` · 関数 `00535828` · 推定シンボル `None` · 推定型 `None`
- [`004eaeb8`](#insn-004eaeb8) → `00c9aa28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004eaeb8`](#insn-004eaeb8) → `00c65ff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan12Lookup_ErrorE` · 推定型 `pointer __((offset(0x10)))`
- [`004eaec0`](#insn-004eaec0) → [`00c57b10`](../00c57/00c57b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b10` · 推定シンボル `None` · 推定型 `None`
- [`004eaf54`](#insn-004eaf54) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004eadd0`](#insn-004eadd0)

~~~json
{
  "source": "004eadd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eadd4`](#insn-004eadd4)

~~~json
{
  "source": "004eadd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eadd8`](#insn-004eadd8)

~~~json
{
  "source": "004eadd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eaddc`](#insn-004eaddc)

~~~json
{
  "source": "004eaddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eadf4`](#insn-004eadf4)

~~~json
{
  "source": "004eadf4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eadf8`](#insn-004eadf8)

~~~json
{
  "source": "004eadf8",
  "target": "00c57af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eae20`](#insn-004eae20)

~~~json
{
  "source": "004eae20",
  "target": "002b81c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b81c8",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "20646f6573206e6f7420737570706f7274207369676e61747572657300",
  "capture_start": "002b81c8",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004eae28`](#insn-004eae28)

~~~json
{
  "source": "004eae28",
  "target": "00c57b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eae3c`](#insn-004eae3c)

~~~json
{
  "source": "004eae3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae44`](#insn-004eae44)

~~~json
{
  "source": "004eae44",
  "target": "Stack[-0x4d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae48`](#insn-004eae48)

~~~json
{
  "source": "004eae48",
  "target": "00c9a9d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a9d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004eae5c`](#insn-004eae5c)

~~~json
{
  "source": "004eae5c",
  "target": "00c67028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67018",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004eae60`](#insn-004eae60)

~~~json
{
  "source": "004eae60",
  "target": "004eae80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae64`](#insn-004eae64)

~~~json
{
  "source": "004eae64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae68`](#insn-004eae68)

~~~json
{
  "source": "004eae68",
  "target": "Stack[-0x4d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae7c`](#insn-004eae7c)

~~~json
{
  "source": "004eae7c",
  "target": "004eae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eae88`](#insn-004eae88)

~~~json
{
  "source": "004eae88",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eae90`](#insn-004eae90)

~~~json
{
  "source": "004eae90",
  "target": "00c9abf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004eae98`](#insn-004eae98)

~~~json
{
  "source": "004eae98",
  "target": "00c67078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67068",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004eaea0`](#insn-004eaea0)

~~~json
{
  "source": "004eaea0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eaea8`](#insn-004eaea8)

~~~json
{
  "source": "004eaea8",
  "target": "004eaf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eaeb4`](#insn-004eaeb4)

~~~json
{
  "source": "004eaeb4",
  "target": "00535828",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eaeb8`](#insn-004eaeb8)

~~~json
{
  "source": "004eaeb8",
  "target": "00c9aa28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aa28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004eaeb8`](#insn-004eaeb8)

~~~json
{
  "source": "004eaeb8",
  "target": "00c65ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65ff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004eaec0`](#insn-004eaec0)

~~~json
{
  "source": "004eaec0",
  "target": "00c57b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eaf54`](#insn-004eaf54)

~~~json
{
  "source": "004eaf54",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
