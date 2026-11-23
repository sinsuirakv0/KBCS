# 00babd1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00babc54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00babc54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-6226a4c168536e7424eedf989232ae91)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00babd60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babd60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-41927b256c86cc8ce71faaec2b594c50)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babd1c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab5b8fb3ac083131cbeae40af3da646fa25145be096031b831711115492a527f",
  "source_text_sha256": "ab5b8fb3ac083131cbeae40af3da646fa25145be096031b831711115492a527f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babd1c",
        "00babd77"
      ]
    ],
    "bytes_sha256": "c7b818276f3b7bb64c101f26c79e44fccf44afe7c9b302f8a18396fb848d9fdf",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1530](../00be1/00be1530.md)
- [00be1b40](../00be1/00be1b40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 851 bytes

~~~c

ulong _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv(long param_1)

{
  __locale_t __dataset;
  size_t sVar1;
  
                    /* catch() { ... } // from try @ 00bab7ec with catch @ 00babd20 */
                    /* catch() { ... } // from try @ 00bab7bc with catch @ 00babd28 */
                    /* catch() { ... } // from try @ 00bab954 with catch @ 00babd30 */
                    /* catch() { ... } // from try @ 00babac8 with catch @ 00babd34 */
  if (*(__locale_t *)(param_1 + 0x10) == (__locale_t)0x0) {
    sVar1 = 1;
  }
  else {
    __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
                    /* catch() { ... } // from try @ 00bab80c with catch @ 00babd44 */
    sVar1 = __ctype_get_mb_cur_max();
    if (__dataset != (__locale_t)0x0) {
      uselocale(__dataset);
    }
  }
  return sVar1 & 0xffffffff;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babd1c"></a> `00babd1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00babd20"></a> `00babd20` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babd24"></a> `00babd24` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babd28"></a> `00babd28` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babd2c"></a> `00babd2c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00babd30"></a> `00babd30` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00babd34"></a> `00babd34` | `40 01 00 b4` | cbz x0,0x00babd5c | `CONDITIONAL_JUMP`
<a id="insn-00babd38"></a> `00babd38` | `fe d5 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00babd3c"></a> `00babd3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00babd40"></a> `00babd40` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babd44"></a> `00babd44` | `7f d7 00 94` | bl 0x00be1b40 | `UNCONDITIONAL_CALL`
<a id="insn-00babd48"></a> `00babd48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babd4c"></a> `00babd4c` | `b4 00 00 b4` | cbz x20,0x00babd60 | `CONDITIONAL_JUMP`
<a id="insn-00babd50"></a> `00babd50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00babd54"></a> `00babd54` | `f7 d5 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00babd58"></a> `00babd58` | `02 00 00 14` | b 0x00babd60 | `UNCONDITIONAL_JUMP`
<a id="insn-00babd5c"></a> `00babd5c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00babd60"></a> `00babd60` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00babd64"></a> `00babd64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babd68"></a> `00babd68` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babd6c"></a> `00babd6c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babd70"></a> `00babd70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00babd74"></a> `00babd74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babd1c`](#insn-00babd1c) 範囲 `[['00babd1c', '00babd1f']]`
  - `FALL_THROUGH` [`00babd1c`](#insn-00babd1c) → [`00babd20`](#insn-00babd20)
- ブロック [`00babd20`](#insn-00babd20) 範囲 `[['00babd20', '00babd27']]`
  - `FALL_THROUGH` [`00babd24`](#insn-00babd24) → [`00babd28`](#insn-00babd28)
- ブロック [`00babd28`](#insn-00babd28) 範囲 `[['00babd28', '00babd2f']]`
  - `FALL_THROUGH` [`00babd2c`](#insn-00babd2c) → [`00babd30`](#insn-00babd30)
- ブロック [`00babd30`](#insn-00babd30) 範囲 `[['00babd30', '00babd33']]`
  - `FALL_THROUGH` [`00babd30`](#insn-00babd30) → [`00babd34`](#insn-00babd34)
- ブロック [`00babd34`](#insn-00babd34) 範囲 `[['00babd34', '00babd37']]`
  - `CONDITIONAL_JUMP` [`00babd34`](#insn-00babd34) → [`00babd5c`](#insn-00babd5c)
  - `FALL_THROUGH` [`00babd34`](#insn-00babd34) → [`00babd38`](#insn-00babd38)
- ブロック [`00babd38`](#insn-00babd38) 範囲 `[['00babd38', '00babd43']]`
  - `FALL_THROUGH` [`00babd40`](#insn-00babd40) → [`00babd44`](#insn-00babd44)
- ブロック [`00babd44`](#insn-00babd44) 範囲 `[['00babd44', '00babd4f']]`
  - `CONDITIONAL_JUMP` [`00babd4c`](#insn-00babd4c) → [`00babd60`](#insn-00babd60)
  - `FALL_THROUGH` [`00babd4c`](#insn-00babd4c) → [`00babd50`](#insn-00babd50)
- ブロック [`00babd50`](#insn-00babd50) 範囲 `[['00babd50', '00babd5b']]`
  - `UNCONDITIONAL_JUMP` [`00babd58`](#insn-00babd58) → [`00babd60`](#insn-00babd60)
- ブロック [`00babd5c`](#insn-00babd5c) 範囲 `[['00babd5c', '00babd5f']]`
  - `FALL_THROUGH` [`00babd5c`](#insn-00babd5c) → [`00babd60`](#insn-00babd60)
- ブロック [`00babd60`](#insn-00babd60) 範囲 `[['00babd60', '00babd77']]`

## 命令位置別の参照

- [`00babd24`](#insn-00babd24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd28`](#insn-00babd28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd34`](#insn-00babd34) → [`00babd5c`](#insn-00babd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd38`](#insn-00babd38) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00babd40`](#insn-00babd40) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd44`](#insn-00babd44) → [`00be1b40`](../00be1/00be1b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b40` · 推定シンボル `None` · 推定型 `None`
- [`00babd4c`](#insn-00babd4c) → [`00babd60`](#insn-00babd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd54`](#insn-00babd54) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00babd58`](#insn-00babd58) → [`00babd60`](#insn-00babd60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd64`](#insn-00babd64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd68`](#insn-00babd68) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babd24`](#insn-00babd24)

~~~json
{
  "source": "00babd24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd28`](#insn-00babd28)

~~~json
{
  "source": "00babd28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd34`](#insn-00babd34)

~~~json
{
  "source": "00babd34",
  "target": "00babd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd38`](#insn-00babd38)

~~~json
{
  "source": "00babd38",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd40`](#insn-00babd40)

~~~json
{
  "source": "00babd40",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd44`](#insn-00babd44)

~~~json
{
  "source": "00babd44",
  "target": "00be1b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd4c`](#insn-00babd4c)

~~~json
{
  "source": "00babd4c",
  "target": "00babd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd54`](#insn-00babd54)

~~~json
{
  "source": "00babd54",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd58`](#insn-00babd58)

~~~json
{
  "source": "00babd58",
  "target": "00babd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd64`](#insn-00babd64)

~~~json
{
  "source": "00babd64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd68`](#insn-00babd68)

~~~json
{
  "source": "00babd68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
