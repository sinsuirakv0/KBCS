# 00bba5bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bba684`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-4e9af87cc9d8e24e2c914d08060c7284)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba5bc",
  "name": "__cxa_throw_bad_array_new_length",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f22a776c4ba7d77827f046f895bafa4bba42960d478705cddec3365fe39347a6",
  "source_text_sha256": "f22a776c4ba7d77827f046f895bafa4bba42960d478705cddec3365fe39347a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba5bc",
        "00bba5f3"
      ]
    ],
    "bytes_sha256": "adbed55e41f6a883378f0b8697b5071755db7dcc0db27a34ec893bb9a748ea60",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdafa0](../00bda/00bdafa0.md)
- [00bdafc0](../00bda/00bdafc0.md)
- [00bdb0e0](../00bdb/00bdb0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 597 bytes

~~~c

void __cxa_throw_bad_array_new_length(void)

{
  undefined8 uVar1;
  
                    /* catch() { ... } // from try @ 00bb6d68 with catch @ 00bba5cc */
  uVar1 = __cxa_allocate_exception(8);
  _ZNSt20bad_array_new_lengthC1Ev();
                    /* catch() { ... } // from try @ 00bb6d5c with catch @ 00bba5e0 */
                    /* catch() { ... } // from try @ 00bb69c4 with catch @ 00bba5e4 */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTISt20bad_array_new_length_00c1ace0,
              PTR__ZNSt20bad_array_new_lengthD1Ev_00c1ace8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba5bc"></a> `00bba5bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bba5c0"></a> `00bba5c0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba5c4"></a> `00bba5c4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba5c8"></a> `00bba5c8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bba5cc"></a> `00bba5cc` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bba5d0"></a> `00bba5d0` | `74 82 00 94` | bl 0x00bdafa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba5d4"></a> `00bba5d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bba5d8"></a> `00bba5d8` | `c2 82 00 94` | bl 0x00bdb0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba5dc"></a> `00bba5dc` | `01 03 00 90` | adrp x1,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bba5e0"></a> `00bba5e0` | `02 03 00 90` | adrp x2,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bba5e4"></a> `00bba5e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bba5e8"></a> `00bba5e8` | `21 70 46 f9` | ldr x1,[x1, #0xce0] | `FALL_THROUGH`
<a id="insn-00bba5ec"></a> `00bba5ec` | `42 74 46 f9` | ldr x2,[x2, #0xce8] | `FALL_THROUGH`
<a id="insn-00bba5f0"></a> `00bba5f0` | `74 82 00 94` | bl 0x00bdafc0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba5bc`](#insn-00bba5bc) 範囲 `[['00bba5bc', '00bba5cb']]`
  - `FALL_THROUGH` [`00bba5c8`](#insn-00bba5c8) → [`00bba5cc`](#insn-00bba5cc)
- ブロック [`00bba5cc`](#insn-00bba5cc) 範囲 `[['00bba5cc', '00bba5df']]`
  - `FALL_THROUGH` [`00bba5dc`](#insn-00bba5dc) → [`00bba5e0`](#insn-00bba5e0)
- ブロック [`00bba5e0`](#insn-00bba5e0) 範囲 `[['00bba5e0', '00bba5e3']]`
  - `FALL_THROUGH` [`00bba5e0`](#insn-00bba5e0) → [`00bba5e4`](#insn-00bba5e4)
- ブロック [`00bba5e4`](#insn-00bba5e4) 範囲 `[['00bba5e4', '00bba5f3']]`

## 命令位置別の参照

- [`00bba5c0`](#insn-00bba5c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba5c4`](#insn-00bba5c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba5d0`](#insn-00bba5d0) → [`00bdafa0`](../00bda/00bdafa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafa0` · 推定シンボル `None` · 推定型 `None`
- [`00bba5d8`](#insn-00bba5d8) → [`00bdb0e0`](../00bdb/00bdb0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0e0` · 推定シンボル `None` · 推定型 `None`
- [`00bba5e8`](#insn-00bba5e8) → `00c1ace0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bba5e8`](#insn-00bba5e8) → `00c16808`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt20bad_array_new_length` · 推定型 `pointer __((offset(0x10)))`
- [`00bba5ec`](#insn-00bba5ec) → `00c1ace8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bba5ec`](#insn-00bba5ec) → [`00bbac28`](00bbac28.md) · `PARAM` · `ANALYSIS` · 関数 `00bbac28` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`00bba5f0`](#insn-00bba5f0) → [`00bdafc0`](../00bda/00bdafc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafc0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba5c0`](#insn-00bba5c0)

~~~json
{
  "source": "00bba5c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba5c4`](#insn-00bba5c4)

~~~json
{
  "source": "00bba5c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba5d0`](#insn-00bba5d0)

~~~json
{
  "source": "00bba5d0",
  "target": "00bdafa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba5d8`](#insn-00bba5d8)

~~~json
{
  "source": "00bba5d8",
  "target": "00bdb0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba5e8`](#insn-00bba5e8)

~~~json
{
  "source": "00bba5e8",
  "target": "00c1ace0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ace0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bba5e8`](#insn-00bba5e8)

~~~json
{
  "source": "00bba5e8",
  "target": "00c16808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bba5ec`](#insn-00bba5ec)

~~~json
{
  "source": "00bba5ec",
  "target": "00c1ace8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ace8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bba5ec`](#insn-00bba5ec)

~~~json
{
  "source": "00bba5ec",
  "target": "00bbac28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba5f0`](#insn-00bba5f0)

~~~json
{
  "source": "00bba5f0",
  "target": "00bdafc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
