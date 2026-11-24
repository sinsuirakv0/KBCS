# 00bc9ccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5a7cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a7cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-5c1e47a59dd0e98c3aac396722ae0f6e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bca0f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-240a2158049cce82b0d406767d9161f0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9ccc",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b7f65ea0aa637fe5243d5351675bad18f4715e6d16267c7e22c7dcef10a41ae",
  "source_text_sha256": "6b7f65ea0aa637fe5243d5351675bad18f4715e6d16267c7e22c7dcef10a41ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9ccc",
        "00bc9d4b"
      ]
    ],
    "bytes_sha256": "69425deeea8e6e49b5f089ef3a396280e8ef2bbcfb0172f382ff90448f324910",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a800](../00c5a/00c5a800.md)
- [00c5a810](../00c5a/00c5a810.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1509 bytes

~~~c

void _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_
               (long *param_1,long param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00bc9acc with catch @ 00bc9cd0 */
                    /* catch() { ... } // from try @ 00bc99fc with catch @ 00bc9cd8 */
                    /* catch() { ... } // from try @ 00bc9a1c with catch @ 00bc9ce0 */
                    /* catch() { ... } // from try @ 00bc9bc4 with catch @ 00bc9ce4 */
  *param_1 = (long)(PTR__ZTVN8firebase13remote_config32ConfigUpdateListenerRegistrationE_00c9b528 +
                   0x10);
  param_1[1] = *(long *)(param_2 + 8);
  param_1[2] = 0;
  lVar1 = 0;
  if (*(long *)(param_2 + 8) != 0) {
    _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_2 + 8) + 0x138,param_2);
    lVar1 = param_1[2];
  }
  param_1[2] = *(long *)(param_2 + 0x10);
  *(long *)(param_2 + 0x10) = lVar1;
  if (param_1[1] != 0) {
                    /* catch() { ... } // from try @ 00bc99e4 with catch @ 00bc9d24
                       catch() { ... } // from try @ 00bc9b9c with catch @ 00bc9d24 */
                    /* catch() { ... } // from try @ 00bc9aec with catch @ 00bc9d2c */
    _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
              (param_1[1] + 0x138,param_1,
               PTR__ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv_00c9b520
              );
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc9ccc"></a> `00bc9ccc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc9cd0"></a> `00bc9cd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9cd4"></a> `00bc9cd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc9cd8"></a> `00bc9cd8` | `88 06 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bc9cdc"></a> `00bc9cdc` | `08 95 42 f9` | ldr x8,[x8, #0x528] | `FALL_THROUGH`
<a id="insn-00bc9ce0"></a> `00bc9ce0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bc9ce4"></a> `00bc9ce4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc9ce8"></a> `00bc9ce8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bc9cec"></a> `00bc9cec` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc9cf0"></a> `00bc9cf0` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9cf4"></a> `00bc9cf4` | `08 fc 00 a9` | stp x8,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9cf8"></a> `00bc9cf8` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9cfc"></a> `00bc9cfc` | `a8 00 00 b4` | cbz x8,0x00bc9d10 | `CONDITIONAL_JUMP`
<a id="insn-00bc9d00"></a> `00bc9d00` | `00 e1 04 91` | add x0,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00bc9d04"></a> `00bc9d04` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc9d08"></a> `00bc9d08` | `c2 42 02 94` | bl 0x00c5a810 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d0c"></a> `00bc9d0c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d10"></a> `00bc9d10` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d14"></a> `00bc9d14` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d18"></a> `00bc9d18` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d1c"></a> `00bc9d1c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9d20"></a> `00bc9d20` | `08 01 00 b4` | cbz x8,0x00bc9d40 | `CONDITIONAL_JUMP`
<a id="insn-00bc9d24"></a> `00bc9d24` | `82 06 00 d0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bc9d28"></a> `00bc9d28` | `42 90 42 f9` | ldr x2,[x2, #0x520] | `FALL_THROUGH`
<a id="insn-00bc9d2c"></a> `00bc9d2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d30"></a> `00bc9d30` | `00 e1 04 91` | add x0,x8,#0x138 | `FALL_THROUGH`
<a id="insn-00bc9d34"></a> `00bc9d34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc9d38"></a> `00bc9d38` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc9d3c"></a> `00bc9d3c` | `b1 42 02 14` | b 0x00c5a800 | `CALL_TERMINATOR`
<a id="insn-00bc9d40"></a> `00bc9d40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d44"></a> `00bc9d44` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc9d48"></a> `00bc9d48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9ccc`](#insn-00bc9ccc) 範囲 `[['00bc9ccc', '00bc9ccf']]`
  - `FALL_THROUGH` [`00bc9ccc`](#insn-00bc9ccc) → [`00bc9cd0`](#insn-00bc9cd0)
- ブロック [`00bc9cd0`](#insn-00bc9cd0) 範囲 `[['00bc9cd0', '00bc9cd7']]`
  - `FALL_THROUGH` [`00bc9cd4`](#insn-00bc9cd4) → [`00bc9cd8`](#insn-00bc9cd8)
- ブロック [`00bc9cd8`](#insn-00bc9cd8) 範囲 `[['00bc9cd8', '00bc9cdf']]`
  - `FALL_THROUGH` [`00bc9cdc`](#insn-00bc9cdc) → [`00bc9ce0`](#insn-00bc9ce0)
- ブロック [`00bc9ce0`](#insn-00bc9ce0) 範囲 `[['00bc9ce0', '00bc9ce3']]`
  - `FALL_THROUGH` [`00bc9ce0`](#insn-00bc9ce0) → [`00bc9ce4`](#insn-00bc9ce4)
- ブロック [`00bc9ce4`](#insn-00bc9ce4) 範囲 `[['00bc9ce4', '00bc9cff']]`
  - `CONDITIONAL_JUMP` [`00bc9cfc`](#insn-00bc9cfc) → [`00bc9d10`](#insn-00bc9d10)
  - `FALL_THROUGH` [`00bc9cfc`](#insn-00bc9cfc) → [`00bc9d00`](#insn-00bc9d00)
- ブロック [`00bc9d00`](#insn-00bc9d00) 範囲 `[['00bc9d00', '00bc9d0f']]`
  - `FALL_THROUGH` [`00bc9d0c`](#insn-00bc9d0c) → [`00bc9d10`](#insn-00bc9d10)
- ブロック [`00bc9d10`](#insn-00bc9d10) 範囲 `[['00bc9d10', '00bc9d23']]`
  - `CONDITIONAL_JUMP` [`00bc9d20`](#insn-00bc9d20) → [`00bc9d40`](#insn-00bc9d40)
  - `FALL_THROUGH` [`00bc9d20`](#insn-00bc9d20) → [`00bc9d24`](#insn-00bc9d24)
- ブロック [`00bc9d24`](#insn-00bc9d24) 範囲 `[['00bc9d24', '00bc9d2b']]`
  - `FALL_THROUGH` [`00bc9d28`](#insn-00bc9d28) → [`00bc9d2c`](#insn-00bc9d2c)
- ブロック [`00bc9d2c`](#insn-00bc9d2c) 範囲 `[['00bc9d2c', '00bc9d3f']]`
- ブロック [`00bc9d40`](#insn-00bc9d40) 範囲 `[['00bc9d40', '00bc9d4b']]`

## 命令位置別の参照

- [`00bc9ccc`](#insn-00bc9ccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cd0`](#insn-00bc9cd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cdc`](#insn-00bc9cdc) → `00c9b528`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc9cec`](#insn-00bc9cec) → `00c914a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[32]`
- [`00bc9cfc`](#insn-00bc9cfc) → [`00bc9d10`](#insn-00bc9d10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d08`](#insn-00bc9d08) → [`00c5a810`](../00c5a/00c5a810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a810` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d20`](#insn-00bc9d20) → [`00bc9d40`](#insn-00bc9d40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d28`](#insn-00bc9d28) → `00c9b520`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc9d28`](#insn-00bc9d28) → [`00bc9f38`](00bc9f38.md) · `PARAM` · `ANALYSIS` · 関数 `00bc9f38` · 推定シンボル `_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv` · 推定型 `None`
- [`00bc9d2c`](#insn-00bc9d2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d3c`](#insn-00bc9d3c) → [`00c5a800`](../00c5a/00c5a800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a800` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d40`](#insn-00bc9d40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9ccc`](#insn-00bc9ccc)

~~~json
{
  "source": "00bc9ccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9cd0`](#insn-00bc9cd0)

~~~json
{
  "source": "00bc9cd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9cdc`](#insn-00bc9cdc)

~~~json
{
  "source": "00bc9cdc",
  "target": "00c9b528",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b528",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc9cec`](#insn-00bc9cec)

~~~json
{
  "source": "00bc9cec",
  "target": "00c914a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91498",
  "offset": 16,
  "size": 32,
  "datatype": "undefined1[32]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bc9cfc`](#insn-00bc9cfc)

~~~json
{
  "source": "00bc9cfc",
  "target": "00bc9d10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d08`](#insn-00bc9d08)

~~~json
{
  "source": "00bc9d08",
  "target": "00c5a810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d20`](#insn-00bc9d20)

~~~json
{
  "source": "00bc9d20",
  "target": "00bc9d40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d28`](#insn-00bc9d28)

~~~json
{
  "source": "00bc9d28",
  "target": "00c9b520",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b520",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc9d28`](#insn-00bc9d28)

~~~json
{
  "source": "00bc9d28",
  "target": "00bc9f38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d2c`](#insn-00bc9d2c)

~~~json
{
  "source": "00bc9d2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d3c`](#insn-00bc9d3c)

~~~json
{
  "source": "00bc9d3c",
  "target": "00c5a800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d40`](#insn-00bc9d40)

~~~json
{
  "source": "00bc9d40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
