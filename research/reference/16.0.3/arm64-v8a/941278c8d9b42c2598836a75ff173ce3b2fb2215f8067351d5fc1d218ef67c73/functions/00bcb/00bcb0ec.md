# 00bcb0ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bca0f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-4e44e7d229404d810afd3df176e5289e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb0ec",
  "name": "_INIT_289",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "604bce8a8d4c315b521f55afa122b1fc03cf2af27a223f9b0bc643b9190b35f8",
  "source_text_sha256": "604bce8a8d4c315b521f55afa122b1fc03cf2af27a223f9b0bc643b9190b35f8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb0ec",
        "00bcb12f"
      ]
    ],
    "bytes_sha256": "30cf32593006290890e7fa22c31299fdbeeae314e4a8b04a854c7941995543ea",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58ed0](../00c58/00c58ed0.md)
- [00c5bd20](../00c5b/00c5bd20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 649 bytes

~~~c

void _INIT_289(void)

{
  undefined *puVar1;
  undefined *puVar2;
  
  puVar1 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  puVar2 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 +
           4;
  *(undefined4 *)
   PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 = 0;
  _ZN8firebase5MutexC1ENS0_4ModeE(puVar2,1);
                    /* try { // try from 00bcb124 to 00ccb127 has its CatchHandler @ 00bcb2ac */
  __cxa_atexit(PTR__ZN8firebase8internal14ReferenceCountD2Ev_00c9ca38,puVar1,&PTR_LOOP_00c64030);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb0ec"></a> `00bcb0ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcb0f0"></a> `00bcb0f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb0f4"></a> `00bcb0f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcb0f8"></a> `00bcb0f8` | `93 06 00 b0` | adrp x19,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcb0fc"></a> `00bcb0fc` | `73 0e 45 f9` | ldr x19,[x19, #0xa18] | `FALL_THROUGH`
<a id="insn-00bcb100"></a> `00bcb100` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bcb104"></a> `00bcb104` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb108"></a> `00bcb108` | `1f 44 00 b8` | str wzr,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00bcb10c"></a> `00bcb10c` | `05 43 02 94` | bl 0x00c5bd20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb110"></a> `00bcb110` | `80 06 00 b0` | adrp x0,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bcb114"></a> `00bcb114` | `00 1c 45 f9` | ldr x0,[x0, #0xa38] | `FALL_THROUGH`
<a id="insn-00bcb118"></a> `00bcb118` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb11c"></a> `00bcb11c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bcb120"></a> `00bcb120` | `82 78 4c 10` | adr x2,0xc64030 | `FALL_THROUGH`
<a id="insn-00bcb124"></a> `00bcb124` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcb128"></a> `00bcb128` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcb12c"></a> `00bcb12c` | `69 37 02 14` | b 0x00c58ed0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb0ec`](#insn-00bcb0ec) 範囲 `[['00bcb0ec', '00bcb123']]`
  - `FALL_THROUGH` [`00bcb120`](#insn-00bcb120) → [`00bcb124`](#insn-00bcb124)
- ブロック [`00bcb124`](#insn-00bcb124) 範囲 `[['00bcb124', '00bcb12f']]`

## 命令位置別の参照

- [`00bcb0ec`](#insn-00bcb0ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb0f0`](#insn-00bcb0f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb0fc`](#insn-00bcb0fc) → `00c9ca18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcb108`](#insn-00bcb108) → `01127778`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bcb108`](#insn-00bcb108) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb10c`](#insn-00bcb10c) → [`00c5bd20`](../00c5b/00c5bd20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd20` · 推定シンボル `None` · 推定型 `None`
- [`00bcb114`](#insn-00bcb114) → `00c9ca38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcb114`](#insn-00bcb114) → [`00bc4ca4`](../00bc4/00bc4ca4.md) · `PARAM` · `ANALYSIS` · 関数 `00bc4ca4` · 推定シンボル `_ZN8firebase8internal14ReferenceCountD2Ev` · 推定型 `None`
- [`00bcb118`](#insn-00bcb118) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb120`](#insn-00bcb120) → `00c64030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcb124`](#insn-00bcb124) → `01127778`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bcb12c`](#insn-00bcb12c) → [`00c58ed0`](../00c58/00c58ed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ed0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb0ec`](#insn-00bcb0ec)

~~~json
{
  "source": "00bcb0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb0f0`](#insn-00bcb0f0)

~~~json
{
  "source": "00bcb0f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb0fc`](#insn-00bcb0fc)

~~~json
{
  "source": "00bcb0fc",
  "target": "00c9ca18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb108`](#insn-00bcb108)

~~~json
{
  "source": "00bcb108",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcb108`](#insn-00bcb108)

~~~json
{
  "source": "00bcb108",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb10c`](#insn-00bcb10c)

~~~json
{
  "source": "00bcb10c",
  "target": "00c5bd20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb114`](#insn-00bcb114)

~~~json
{
  "source": "00bcb114",
  "target": "00c9ca38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb114`](#insn-00bcb114)

~~~json
{
  "source": "00bcb114",
  "target": "00bc4ca4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb118`](#insn-00bcb118)

~~~json
{
  "source": "00bcb118",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb120`](#insn-00bcb120)

~~~json
{
  "source": "00bcb120",
  "target": "00c64030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb124`](#insn-00bcb124)

~~~json
{
  "source": "00bcb124",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcb12c`](#insn-00bcb12c)

~~~json
{
  "source": "00bcb12c",
  "target": "00c58ed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
