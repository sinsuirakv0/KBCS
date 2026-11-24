# 00bbbfe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbafec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-bc12d65634f308657ee61f83d53c52eb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfe0",
  "name": "FUN_00bbbfe0",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a1fa926a65111dd2003adfdaa256d85f2cfd32fd545f18b86af06a50091e2ed",
  "source_text_sha256": "9a1fa926a65111dd2003adfdaa256d85f2cfd32fd545f18b86af06a50091e2ed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbfe0",
        "00bbc0b7"
      ]
    ],
    "bytes_sha256": "f8f36e08edb2c6e1e36ee05d9098b8134040c3bd4961519f06180e8f1e10e014",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bbb6b8](../00bbb/00bbb6b8.md)
- [00bbbe34](../00bbb/00bbbe34.md)

## 呼び出し先

- [0087c3c0](../0087c/0087c3c0.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5e660](../00c5e/00c5e660.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1343 bytes

~~~c

void FUN_00bbbfe0(void)

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
  if (DAT_01127420 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
      puVar2 = (undefined8 *)_Znwm(0x10);
      *puVar2 = FUN_00bbe428;
      puVar2[1] = 0;
      (**(code **)(*local_40 + 0x40))
                (auStack_80,local_40,auStack_38,
                 PTR__ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv_00c9c9b0
                 ,puVar2,
                 PTR__ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c9c9a8
                 ,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
    FUN_0087c3c0(auStack_68);
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
<a id="insn-00bbbfe0"></a> `00bbbfe0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbbfe4"></a> `00bbbfe4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbfe8"></a> `00bbbfe8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbfec"></a> `00bbbfec` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bbbff0"></a> `00bbbff0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbbff4"></a> `00bbbff4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbff8"></a> `00bbbff8` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbbffc"></a> `00bbbffc` | `68 2b 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbc000"></a> `00bbc000` | `08 11 42 f9` | ldr x8,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bbc004"></a> `00bbc004` | `c8 03 00 b4` | cbz x8,0x00bbc07c | `CONDITIONAL_JUMP`
<a id="insn-00bbc008"></a> `00bbc008` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc00c"></a> `00bbc00c` | `95 89 02 94` | bl 0x00c5e660 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc010"></a> `00bbc010` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc014"></a> `00bbc014` | `a3 7e 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc018"></a> `00bbc018` | `f3 23 40 f9` | ldr x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbc01c"></a> `00bbc01c` | `73 02 00 b4` | cbz x19,0x00bbc068 | `CONDITIONAL_JUMP`
<a id="insn-00bbc020"></a> `00bbc020` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbc024"></a> `00bbc024` | `c3 73 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc028"></a> `00bbc028` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbc02c"></a> `00bbc02c` | `e8 1f 01 10` | adr x8,0xbbe428 | `FALL_THROUGH`
<a id="insn-00bbc030"></a> `00bbc030` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbc034"></a> `00bbc034` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbc038"></a> `00bbc038` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bbc03c"></a> `00bbc03c` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00bbc040"></a> `00bbc040` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc044"></a> `00bbc044` | `01 c1 00 91` | add x1,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbc048"></a> `00bbc048` | `02 07 00 90` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bbc04c"></a> `00bbc04c` | `04 07 00 90` | adrp x4,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bbc050"></a> `00bbc050` | `42 d8 44 f9` | ldr x2,[x2, #0x9b0] | `FALL_THROUGH`
<a id="insn-00bbc054"></a> `00bbc054` | `84 d4 44 f9` | ldr x4,[x4, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bbc058"></a> `00bbc058` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bbc05c"></a> `00bbc05c` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc060"></a> `00bbc060` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbc064"></a> `00bbc064` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bbc068"></a> `00bbc068` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc06c"></a> `00bbc06c` | `91 7e 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc070"></a> `00bbc070` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc074"></a> `00bbc074` | `d3 00 f3 97` | bl 0x0087c3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc078"></a> `00bbc078` | `07 00 00 14` | b 0x00bbc094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc07c"></a> `00bbc07c` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbc080"></a> `00bbc080` | `00 4c 26 91` | add x0,x0,#0x993 | `FALL_THROUGH`
<a id="insn-00bbc084"></a> `00bbc084` | `2f 7f 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc088"></a> `00bbc088` | `a0 b7 ff 90` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbc08c"></a> `00bbc08c` | `00 c8 1f 91` | add x0,x0,#0x7f2 | `FALL_THROUGH`
<a id="insn-00bbc090"></a> `00bbc090` | `04 80 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc094"></a> `00bbc094` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc098"></a> `00bbc098` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbc09c"></a> `00bbc09c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc0a0"></a> `00bbc0a0` | `a1 00 00 54` | b.ne 0x00bbc0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbc0a4"></a> `00bbc0a4` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbc0a8"></a> `00bbc0a8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbc0ac"></a> `00bbc0ac` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbc0b0"></a> `00bbc0b0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbc0b4"></a> `00bbc0b4` | `b3 73 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbfe0`](#insn-00bbbfe0) 範囲 `[['00bbbfe0', '00bbc007']]`
  - `CONDITIONAL_JUMP` [`00bbc004`](#insn-00bbc004) → [`00bbc07c`](#insn-00bbc07c)
  - `FALL_THROUGH` [`00bbc004`](#insn-00bbc004) → [`00bbc008`](#insn-00bbc008)
- ブロック [`00bbc008`](#insn-00bbc008) 範囲 `[['00bbc008', '00bbc01f']]`
  - `CONDITIONAL_JUMP` [`00bbc01c`](#insn-00bbc01c) → [`00bbc068`](#insn-00bbc068)
  - `FALL_THROUGH` [`00bbc01c`](#insn-00bbc01c) → [`00bbc020`](#insn-00bbc020)
- ブロック [`00bbc020`](#insn-00bbc020) 範囲 `[['00bbc020', '00bbc067']]`
  - `FALL_THROUGH` [`00bbc064`](#insn-00bbc064) → [`00bbc068`](#insn-00bbc068)
- ブロック [`00bbc068`](#insn-00bbc068) 範囲 `[['00bbc068', '00bbc07b']]`
  - `UNCONDITIONAL_JUMP` [`00bbc078`](#insn-00bbc078) → [`00bbc094`](#insn-00bbc094)
- ブロック [`00bbc07c`](#insn-00bbc07c) 範囲 `[['00bbc07c', '00bbc093']]`
  - `FALL_THROUGH` [`00bbc090`](#insn-00bbc090) → [`00bbc094`](#insn-00bbc094)
- ブロック [`00bbc094`](#insn-00bbc094) 範囲 `[['00bbc094', '00bbc0a3']]`
  - `CONDITIONAL_JUMP` [`00bbc0a0`](#insn-00bbc0a0) → [`00bbc0b4`](#insn-00bbc0b4)
  - `FALL_THROUGH` [`00bbc0a0`](#insn-00bbc0a0) → [`00bbc0a4`](#insn-00bbc0a4)
- ブロック [`00bbc0a4`](#insn-00bbc0a4) 範囲 `[['00bbc0a4', '00bbc0b3']]`
- ブロック [`00bbc0b4`](#insn-00bbc0b4) 範囲 `[['00bbc0b4', '00bbc0b7']]`

## 命令位置別の参照

- [`00bbbfe4`](#insn-00bbbfe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfe8`](#insn-00bbbfe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff8`](#insn-00bbbff8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc000`](#insn-00bbc000) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbc004`](#insn-00bbc004) → [`00bbc07c`](#insn-00bbc07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc00c`](#insn-00bbc00c) → [`00c5e660`](../00c5e/00c5e660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e660` · 推定シンボル `None` · 推定型 `None`
- [`00bbc014`](#insn-00bbc014) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc018`](#insn-00bbc018) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc01c`](#insn-00bbc01c) → [`00bbc068`](#insn-00bbc068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc024`](#insn-00bbc024) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbc030`](#insn-00bbc030) → [`00bbe428`](../00bbe/00bbe428.md) · `DATA` · `ANALYSIS` · 関数 `00bbe428` · 推定シンボル `None` · 推定型 `None`
- [`00bbc050`](#insn-00bbc050) → `00c9c9b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc050`](#insn-00bbc050) → [`00bbe404`](../00bbe/00bbe404.md) · `PARAM` · `ANALYSIS` · 関数 `00bbe404` · 推定シンボル `_ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv` · 推定型 `None`
- [`00bbc054`](#insn-00bbc054) → `00c9c9a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc054`](#insn-00bbc054) → [`00bbe41c`](../00bbe/00bbe41c.md) · `PARAM` · `ANALYSIS` · 関数 `00bbe41c` · 推定シンボル `_ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv` · 推定型 `None`
- [`00bbc06c`](#insn-00bbc06c) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc074`](#insn-00bbc074) → [`0087c3c0`](../0087c/0087c3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087c3c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc078`](#insn-00bbc078) → [`00bbc094`](#insn-00bbc094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc080`](#insn-00bbc080) → `002a2993`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc084`](#insn-00bbc084) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bbc08c`](#insn-00bbc08c) → `002b07f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbc090`](#insn-00bbc090) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc098`](#insn-00bbc098) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0a0`](#insn-00bbc0a0) → [`00bbc0b4`](#insn-00bbc0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0a4`](#insn-00bbc0a4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0a8`](#insn-00bbc0a8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0b4`](#insn-00bbc0b4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbfe4`](#insn-00bbbfe4)

~~~json
{
  "source": "00bbbfe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfe8`](#insn-00bbbfe8)

~~~json
{
  "source": "00bbbfe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbff8`](#insn-00bbbff8)

~~~json
{
  "source": "00bbbff8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc000`](#insn-00bbc000)

~~~json
{
  "source": "00bbc000",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbc004`](#insn-00bbc004)

~~~json
{
  "source": "00bbc004",
  "target": "00bbc07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc00c`](#insn-00bbc00c)

~~~json
{
  "source": "00bbc00c",
  "target": "00c5e660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc014`](#insn-00bbc014)

~~~json
{
  "source": "00bbc014",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc018`](#insn-00bbc018)

~~~json
{
  "source": "00bbc018",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc01c`](#insn-00bbc01c)

~~~json
{
  "source": "00bbc01c",
  "target": "00bbc068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc024`](#insn-00bbc024)

~~~json
{
  "source": "00bbc024",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc030`](#insn-00bbc030)

~~~json
{
  "source": "00bbc030",
  "target": "00bbe428",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc050`](#insn-00bbc050)

~~~json
{
  "source": "00bbc050",
  "target": "00c9c9b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c9b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc050`](#insn-00bbc050)

~~~json
{
  "source": "00bbc050",
  "target": "00bbe404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc054`](#insn-00bbc054)

~~~json
{
  "source": "00bbc054",
  "target": "00c9c9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c9a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc054`](#insn-00bbc054)

~~~json
{
  "source": "00bbc054",
  "target": "00bbe41c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc06c`](#insn-00bbc06c)

~~~json
{
  "source": "00bbc06c",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc074`](#insn-00bbc074)

~~~json
{
  "source": "00bbc074",
  "target": "0087c3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc078`](#insn-00bbc078)

~~~json
{
  "source": "00bbc078",
  "target": "00bbc094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc080`](#insn-00bbc080)

~~~json
{
  "source": "00bbc080",
  "target": "002a2993",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2993",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2993",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbc084`](#insn-00bbc084)

~~~json
{
  "source": "00bbc084",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc08c`](#insn-00bbc08c)

~~~json
{
  "source": "00bbc08c",
  "target": "002b07f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b07f2",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b07f2",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbc090`](#insn-00bbc090)

~~~json
{
  "source": "00bbc090",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc098`](#insn-00bbc098)

~~~json
{
  "source": "00bbc098",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0a0`](#insn-00bbc0a0)

~~~json
{
  "source": "00bbc0a0",
  "target": "00bbc0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0a4`](#insn-00bbc0a4)

~~~json
{
  "source": "00bbc0a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0a8`](#insn-00bbc0a8)

~~~json
{
  "source": "00bbc0a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0b4`](#insn-00bbc0b4)

~~~json
{
  "source": "00bbc0b4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
