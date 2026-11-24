# 00bbafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbaf50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-4c3152d5c81e7c53f46cc1d3a2f444bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbbfe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-bc12d65634f308657ee61f83d53c52eb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafec",
  "name": "FUN_00bbafec",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b7bcd5fa9b252715451d3cf3af988e1c53ea8bd24c29682bba192efc8472890",
  "source_text_sha256": "2b7bcd5fa9b252715451d3cf3af988e1c53ea8bd24c29682bba192efc8472890",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafec",
        "00bbb0c3"
      ]
    ],
    "bytes_sha256": "7d7444484d727ffa7231e16df3450bef5ea6b60ec5ae723b6091106b87678388",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bba6c4](../00bba/00bba6c4.md)
- [00bbae40](../00bba/00bbae40.md)

## 呼び出し先

- [0087b414](../0087b/0087b414.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5d690](../00c5d/00c5d690.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1343 bytes

~~~c

void FUN_00bbafec(void)

{
  long lVar1;
  undefined8 *puVar2;
  undefined1 auStack_80 [24];
  undefined1 auStack_68 [40];
  long *local_40;
  undefined1 auStack_38 [16];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
      puVar2 = (undefined8 *)_Znwm(0x10);
      *puVar2 = FUN_00bbd434;
      puVar2[1] = 0;
      (**(code **)(*local_40 + 0x40))
                (auStack_80,local_40,auStack_38,
                 PTR__ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv_00c9b9e0
                 ,puVar2,
                 PTR__ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c9b9d8
                 ,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
    FUN_0087b414(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbafec"></a> `00bbafec` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbaff0"></a> `00bbaff0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbaff4"></a> `00bbaff4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbaff8"></a> `00bbaff8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bbaffc"></a> `00bbaffc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbb000"></a> `00bbb000` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb004"></a> `00bbb004` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbb008"></a> `00bbb008` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb00c"></a> `00bbb00c` | `08 31 42 f9` | ldr x8,[x8, #0x460] | `FALL_THROUGH`
<a id="insn-00bbb010"></a> `00bbb010` | `c8 03 00 b4` | cbz x8,0x00bbb088 | `CONDITIONAL_JUMP`
<a id="insn-00bbb014"></a> `00bbb014` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb018"></a> `00bbb018` | `9e 89 02 94` | bl 0x00c5d690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb01c"></a> `00bbb01c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb020"></a> `00bbb020` | `ac 7e 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb024"></a> `00bbb024` | `f3 23 40 f9` | ldr x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb028"></a> `00bbb028` | `73 02 00 b4` | cbz x19,0x00bbb074 | `CONDITIONAL_JUMP`
<a id="insn-00bbb02c"></a> `00bbb02c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb030"></a> `00bbb030` | `cc 73 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb034"></a> `00bbb034` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbb038"></a> `00bbb038` | `e8 1f 01 10` | adr x8,0xbbd434 | `FALL_THROUGH`
<a id="insn-00bbb03c"></a> `00bbb03c` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbb040"></a> `00bbb040` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb044"></a> `00bbb044` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bbb048"></a> `00bbb048` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb04c"></a> `00bbb04c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb050"></a> `00bbb050` | `01 c1 00 91` | add x1,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbb054"></a> `00bbb054` | `02 07 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bbb058"></a> `00bbb058` | `04 07 00 90` | adrp x4,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bbb05c"></a> `00bbb05c` | `42 f0 44 f9` | ldr x2,[x2, #0x9e0] | `FALL_THROUGH`
<a id="insn-00bbb060"></a> `00bbb060` | `84 ec 44 f9` | ldr x4,[x4, #0x9d8] | `FALL_THROUGH`
<a id="insn-00bbb064"></a> `00bbb064` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bbb068"></a> `00bbb068` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb06c"></a> `00bbb06c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb070"></a> `00bbb070` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bbb074"></a> `00bbb074` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb078"></a> `00bbb078` | `9a 7e 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb07c"></a> `00bbb07c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb080"></a> `00bbb080` | `e5 00 f3 97` | bl 0x0087b414 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb084"></a> `00bbb084` | `07 00 00 14` | b 0x00bbb0a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb088"></a> `00bbb088` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbb08c"></a> `00bbb08c` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbb090"></a> `00bbb090` | `38 7f 02 94` | bl 0x00c5ad70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb094"></a> `00bbb094` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbb098"></a> `00bbb098` | `00 6c 1c 91` | add x0,x0,#0x71b | `FALL_THROUGH`
<a id="insn-00bbb09c"></a> `00bbb09c` | `0d 80 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0a0"></a> `00bbb0a0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb0a4"></a> `00bbb0a4` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbb0a8"></a> `00bbb0a8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbb0ac"></a> `00bbb0ac` | `a1 00 00 54` | b.ne 0x00bbb0c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbb0b0"></a> `00bbb0b0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb0b4"></a> `00bbb0b4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb0b8"></a> `00bbb0b8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb0bc"></a> `00bbb0bc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb0c0"></a> `00bbb0c0` | `bc 73 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafec`](#insn-00bbafec) 範囲 `[['00bbafec', '00bbb013']]`
  - `CONDITIONAL_JUMP` [`00bbb010`](#insn-00bbb010) → [`00bbb088`](#insn-00bbb088)
  - `FALL_THROUGH` [`00bbb010`](#insn-00bbb010) → [`00bbb014`](#insn-00bbb014)
- ブロック [`00bbb014`](#insn-00bbb014) 範囲 `[['00bbb014', '00bbb02b']]`
  - `CONDITIONAL_JUMP` [`00bbb028`](#insn-00bbb028) → [`00bbb074`](#insn-00bbb074)
  - `FALL_THROUGH` [`00bbb028`](#insn-00bbb028) → [`00bbb02c`](#insn-00bbb02c)
- ブロック [`00bbb02c`](#insn-00bbb02c) 範囲 `[['00bbb02c', '00bbb073']]`
  - `FALL_THROUGH` [`00bbb070`](#insn-00bbb070) → [`00bbb074`](#insn-00bbb074)
- ブロック [`00bbb074`](#insn-00bbb074) 範囲 `[['00bbb074', '00bbb087']]`
  - `UNCONDITIONAL_JUMP` [`00bbb084`](#insn-00bbb084) → [`00bbb0a0`](#insn-00bbb0a0)
- ブロック [`00bbb088`](#insn-00bbb088) 範囲 `[['00bbb088', '00bbb09f']]`
  - `FALL_THROUGH` [`00bbb09c`](#insn-00bbb09c) → [`00bbb0a0`](#insn-00bbb0a0)
- ブロック [`00bbb0a0`](#insn-00bbb0a0) 範囲 `[['00bbb0a0', '00bbb0af']]`
  - `CONDITIONAL_JUMP` [`00bbb0ac`](#insn-00bbb0ac) → [`00bbb0c0`](#insn-00bbb0c0)
  - `FALL_THROUGH` [`00bbb0ac`](#insn-00bbb0ac) → [`00bbb0b0`](#insn-00bbb0b0)
- ブロック [`00bbb0b0`](#insn-00bbb0b0) 範囲 `[['00bbb0b0', '00bbb0bf']]`
- ブロック [`00bbb0c0`](#insn-00bbb0c0) 範囲 `[['00bbb0c0', '00bbb0c3']]`

## 命令位置別の参照

- [`00bbaff0`](#insn-00bbaff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff4`](#insn-00bbaff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb004`](#insn-00bbb004) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb00c`](#insn-00bbb00c) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb010`](#insn-00bbb010) → [`00bbb088`](#insn-00bbb088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb018`](#insn-00bbb018) → [`00c5d690`](../00c5d/00c5d690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d690` · 推定シンボル `None` · 推定型 `None`
- [`00bbb020`](#insn-00bbb020) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb024`](#insn-00bbb024) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb028`](#insn-00bbb028) → [`00bbb074`](#insn-00bbb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb030`](#insn-00bbb030) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bbb03c`](#insn-00bbb03c) → [`00bbd434`](../00bbd/00bbd434.md) · `DATA` · `ANALYSIS` · 関数 `00bbd434` · 推定シンボル `None` · 推定型 `None`
- [`00bbb05c`](#insn-00bbb05c) → `00c9b9e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbb05c`](#insn-00bbb05c) → [`00bbd410`](../00bbd/00bbd410.md) · `PARAM` · `ANALYSIS` · 関数 `00bbd410` · 推定シンボル `_ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv` · 推定型 `None`
- [`00bbb060`](#insn-00bbb060) → `00c9b9d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbb060`](#insn-00bbb060) → [`00bbd428`](../00bbd/00bbd428.md) · `PARAM` · `ANALYSIS` · 関数 `00bbd428` · 推定シンボル `_ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv` · 推定型 `None`
- [`00bbb078`](#insn-00bbb078) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb080`](#insn-00bbb080) → [`0087b414`](../0087b/0087b414.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087b414` · 推定シンボル `None` · 推定型 `None`
- [`00bbb084`](#insn-00bbb084) → [`00bbb0a0`](#insn-00bbb0a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb08c`](#insn-00bbb08c) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb090`](#insn-00bbb090) → [`00c5ad70`](../00c5a/00c5ad70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad70` · 推定シンボル `None` · 推定型 `None`
- [`00bbb098`](#insn-00bbb098) → `002b071b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb09c`](#insn-00bbb09c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0a4`](#insn-00bbb0a4) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0ac`](#insn-00bbb0ac) → [`00bbb0c0`](#insn-00bbb0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0b0`](#insn-00bbb0b0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0b4`](#insn-00bbb0b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0c0`](#insn-00bbb0c0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaff0`](#insn-00bbaff0)

~~~json
{
  "source": "00bbaff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaff4`](#insn-00bbaff4)

~~~json
{
  "source": "00bbaff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb004`](#insn-00bbb004)

~~~json
{
  "source": "00bbb004",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb00c`](#insn-00bbb00c)

~~~json
{
  "source": "00bbb00c",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb010`](#insn-00bbb010)

~~~json
{
  "source": "00bbb010",
  "target": "00bbb088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb018`](#insn-00bbb018)

~~~json
{
  "source": "00bbb018",
  "target": "00c5d690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb020`](#insn-00bbb020)

~~~json
{
  "source": "00bbb020",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb024`](#insn-00bbb024)

~~~json
{
  "source": "00bbb024",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb028`](#insn-00bbb028)

~~~json
{
  "source": "00bbb028",
  "target": "00bbb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb030`](#insn-00bbb030)

~~~json
{
  "source": "00bbb030",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb03c`](#insn-00bbb03c)

~~~json
{
  "source": "00bbb03c",
  "target": "00bbd434",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb05c`](#insn-00bbb05c)

~~~json
{
  "source": "00bbb05c",
  "target": "00c9b9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbb05c`](#insn-00bbb05c)

~~~json
{
  "source": "00bbb05c",
  "target": "00bbd410",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb060`](#insn-00bbb060)

~~~json
{
  "source": "00bbb060",
  "target": "00c9b9d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbb060`](#insn-00bbb060)

~~~json
{
  "source": "00bbb060",
  "target": "00bbd428",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb078`](#insn-00bbb078)

~~~json
{
  "source": "00bbb078",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb080`](#insn-00bbb080)

~~~json
{
  "source": "00bbb080",
  "target": "0087b414",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb084`](#insn-00bbb084)

~~~json
{
  "source": "00bbb084",
  "target": "00bbb0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb08c`](#insn-00bbb08c)

~~~json
{
  "source": "00bbb08c",
  "target": "002a28c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a28c8",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a28c8",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb090`](#insn-00bbb090)

~~~json
{
  "source": "00bbb090",
  "target": "00c5ad70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb098`](#insn-00bbb098)

~~~json
{
  "source": "00bbb098",
  "target": "002b071b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b071b",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b071b",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb09c`](#insn-00bbb09c)

~~~json
{
  "source": "00bbb09c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0a4`](#insn-00bbb0a4)

~~~json
{
  "source": "00bbb0a4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0ac`](#insn-00bbb0ac)

~~~json
{
  "source": "00bbb0ac",
  "target": "00bbb0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0b0`](#insn-00bbb0b0)

~~~json
{
  "source": "00bbb0b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0b4`](#insn-00bbb0b4)

~~~json
{
  "source": "00bbb0b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0c0`](#insn-00bbb0c0)

~~~json
{
  "source": "00bbb0c0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
