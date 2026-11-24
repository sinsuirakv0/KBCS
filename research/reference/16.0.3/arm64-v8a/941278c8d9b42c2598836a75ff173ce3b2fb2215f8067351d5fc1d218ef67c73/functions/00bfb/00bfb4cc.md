# 00bfb4cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa4d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-8345e3777fd66e3d0ed977a304b9e064)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb4cc",
  "name": "_ZNSt6__ndk111timed_mutex6unlockEv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f4cfe0d12c79d7f713952587c85dd7a626e10573e22cf248a6a34fc40c87ebe",
  "source_text_sha256": "9f4cfe0d12c79d7f713952587c85dd7a626e10573e22cf248a6a34fc40c87ebe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb4cc",
        "00bfb517"
      ]
    ],
    "bytes_sha256": "ef0f33ff2f10f4fde54b39289a623a6dca36ddbee5eca31fcf35527d1e34bef2",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c591c0](../00c59/00c591c0.md)
- [00c5a1b0](../00c5a/00c5a1b0.md)
- [00c5c740](../00c5c/00c5c740.md)
- [00c5c750](../00c5c/00c5c750.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 456 bytes

~~~c

int _ZNSt6__ndk111timed_mutex6unlockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    *(undefined1 *)((long)param_1 + 0x58) = 0;
    _ZNSt6__ndk118condition_variable10notify_oneEv(param_1 + 1);
    iVar1 = pthread_mutex_unlock(param_1);
    return iVar1;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb4cc"></a> `00bfb4cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb4d0"></a> `00bfb4d0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfb4d4"></a> `00bfb4d4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb4d8"></a> `00bfb4d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb4dc"></a> `00bfb4dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb4e0"></a> `00bfb4e0` | `98 84 01 94` | bl 0x00c5c740 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb4e4"></a> `00bfb4e4` | `40 01 00 35` | cbnz w0,0x00bfb50c | `CONDITIONAL_JUMP`
<a id="insn-00bfb4e8"></a> `00bfb4e8` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfb4ec"></a> `00bfb4ec` | `7f 62 01 39` | strb wzr,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb4f0"></a> `00bfb4f0` | `30 7b 01 94` | bl 0x00c5a1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb4f4"></a> `00bfb4f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfb4f8"></a> `00bfb4f8` | `96 84 01 94` | bl 0x00c5c750 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb4fc"></a> `00bfb4fc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb500"></a> `00bfb500` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfb504"></a> `00bfb504` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb508"></a> `00bfb508` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb50c"></a> `00bfb50c` | `a1 b5 ff d0` | adrp x1,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bfb510"></a> `00bfb510` | `21 64 20 91` | add x1,x1,#0x819 | `FALL_THROUGH`
<a id="insn-00bfb514"></a> `00bfb514` | `2b 77 01 94` | bl 0x00c591c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb4cc`](#insn-00bfb4cc) 範囲 `[['00bfb4cc', '00bfb4e7']]`
  - `CONDITIONAL_JUMP` [`00bfb4e4`](#insn-00bfb4e4) → [`00bfb50c`](#insn-00bfb50c)
  - `FALL_THROUGH` [`00bfb4e4`](#insn-00bfb4e4) → [`00bfb4e8`](#insn-00bfb4e8)
- ブロック [`00bfb4e8`](#insn-00bfb4e8) 範囲 `[['00bfb4e8', '00bfb50b']]`
- ブロック [`00bfb50c`](#insn-00bfb50c) 範囲 `[['00bfb50c', '00bfb517']]`

## 命令位置別の参照

- [`00bfb4d0`](#insn-00bfb4d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4d4`](#insn-00bfb4d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4e0`](#insn-00bfb4e0) → [`00c5c740`](../00c5c/00c5c740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c740` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4e4`](#insn-00bfb4e4) → [`00bfb50c`](#insn-00bfb50c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4f0`](#insn-00bfb4f0) → [`00c5a1b0`](../00c5a/00c5a1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4f8`](#insn-00bfb4f8) → [`00c5c750`](../00c5c/00c5c750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c750` · 推定シンボル `None` · 推定型 `None`
- [`00bfb4fc`](#insn-00bfb4fc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb500`](#insn-00bfb500) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb510`](#insn-00bfb510) → `002b1819`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfb514`](#insn-00bfb514) → [`00c591c0`](../00c59/00c591c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb4d0`](#insn-00bfb4d0)

~~~json
{
  "source": "00bfb4d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb4d4`](#insn-00bfb4d4)

~~~json
{
  "source": "00bfb4d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb4e0`](#insn-00bfb4e0)

~~~json
{
  "source": "00bfb4e0",
  "target": "00c5c740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb4e4`](#insn-00bfb4e4)

~~~json
{
  "source": "00bfb4e4",
  "target": "00bfb50c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb4f0`](#insn-00bfb4f0)

~~~json
{
  "source": "00bfb4f0",
  "target": "00c5a1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb4f8`](#insn-00bfb4f8)

~~~json
{
  "source": "00bfb4f8",
  "target": "00c5c750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb4fc`](#insn-00bfb4fc)

~~~json
{
  "source": "00bfb4fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb500`](#insn-00bfb500)

~~~json
{
  "source": "00bfb500",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb510`](#insn-00bfb510)

~~~json
{
  "source": "00bfb510",
  "target": "002b1819",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1819",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6d75746578206c6f636b206661696c656400",
  "capture_start": "002b1819",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfb514`](#insn-00bfb514)

~~~json
{
  "source": "00bfb514",
  "target": "00c591c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
