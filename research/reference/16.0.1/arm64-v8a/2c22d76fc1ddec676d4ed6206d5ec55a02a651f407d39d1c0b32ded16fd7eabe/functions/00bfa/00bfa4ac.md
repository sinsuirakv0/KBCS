# 00bfa4ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa084`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-c4c3b00d1a64783b63ec22ca2e65d206)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa548`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-161f0749c7a110a4d2dd1b06742a0cc0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa4ac",
  "name": "_ZNSt6__ndk121recursive_timed_mutexD1Ev",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f146dda18efd3a4c6f248475ebc93775163bb9847d8a0969c4aff79a05d2a02",
  "source_text_sha256": "0f146dda18efd3a4c6f248475ebc93775163bb9847d8a0969c4aff79a05d2a02",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa4ac",
        "00bfa4f7"
      ]
    ],
    "bytes_sha256": "35db30833a4b42a9703751e4f5f550af0d9ebca480560517d6b9f0ace25a8694",
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

- [00c57e60](../00c57/00c57e60.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5b6a0](../00c5b/00c5b6a0.md)
- [00c5b6b0](../00c5b/00c5b6b0.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 428 bytes

~~~c

void _ZNSt6__ndk121recursive_timed_mutexD1Ev(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    pthread_mutex_unlock(param_1);
    _ZNSt6__ndk118condition_variableD2Ev(param_1 + 1);
    _ZNSt6__ndk15mutexD1Ev(param_1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa4ac"></a> `00bfa4ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa4b0"></a> `00bfa4b0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfa4b4"></a> `00bfa4b4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa4b8"></a> `00bfa4b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa4bc"></a> `00bfa4bc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa4c0"></a> `00bfa4c0` | `78 84 01 94` | bl 0x00c5b6a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa4c4"></a> `00bfa4c4` | `40 01 00 35` | cbnz w0,0x00bfa4ec | `CONDITIONAL_JUMP`
<a id="insn-00bfa4c8"></a> `00bfa4c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa4cc"></a> `00bfa4cc` | `79 84 01 94` | bl 0x00c5b6b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa4d0"></a> `00bfa4d0` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfa4d4"></a> `00bfa4d4` | `ff 76 01 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa4d8"></a> `00bfa4d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa4dc"></a> `00bfa4dc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa4e0"></a> `00bfa4e0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa4e4"></a> `00bfa4e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa4e8"></a> `00bfa4e8` | `5e 76 01 14` | b 0x00c57e60 | `CALL_TERMINATOR`
<a id="insn-00bfa4ec"></a> `00bfa4ec` | `a1 b5 ff f0` | adrp x1,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bfa4f0"></a> `00bfa4f0` | `21 78 1e 91` | add x1,x1,#0x79e | `FALL_THROUGH`
<a id="insn-00bfa4f4"></a> `00bfa4f4` | `0b 77 01 94` | bl 0x00c58120 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa4ac`](#insn-00bfa4ac) 範囲 `[['00bfa4ac', '00bfa4c7']]`
  - `CONDITIONAL_JUMP` [`00bfa4c4`](#insn-00bfa4c4) → [`00bfa4ec`](#insn-00bfa4ec)
  - `FALL_THROUGH` [`00bfa4c4`](#insn-00bfa4c4) → [`00bfa4c8`](#insn-00bfa4c8)
- ブロック [`00bfa4c8`](#insn-00bfa4c8) 範囲 `[['00bfa4c8', '00bfa4eb']]`
- ブロック [`00bfa4ec`](#insn-00bfa4ec) 範囲 `[['00bfa4ec', '00bfa4f7']]`

## 命令位置別の参照

- [`00bfa4b0`](#insn-00bfa4b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4b4`](#insn-00bfa4b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4c0`](#insn-00bfa4c0) → [`00c5b6a0`](../00c5b/00c5b6a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4c4`](#insn-00bfa4c4) → [`00bfa4ec`](#insn-00bfa4ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4cc`](#insn-00bfa4cc) → [`00c5b6b0`](../00c5b/00c5b6b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4d4`](#insn-00bfa4d4) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4dc`](#insn-00bfa4dc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4e0`](#insn-00bfa4e0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4e8`](#insn-00bfa4e8) → [`00c57e60`](../00c57/00c57e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e60` · 推定シンボル `None` · 推定型 `None`
- [`00bfa4f0`](#insn-00bfa4f0) → `002b179e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfa4f4`](#insn-00bfa4f4) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa4b0`](#insn-00bfa4b0)

~~~json
{
  "source": "00bfa4b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa4b4`](#insn-00bfa4b4)

~~~json
{
  "source": "00bfa4b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa4c0`](#insn-00bfa4c0)

~~~json
{
  "source": "00bfa4c0",
  "target": "00c5b6a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa4c4`](#insn-00bfa4c4)

~~~json
{
  "source": "00bfa4c4",
  "target": "00bfa4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa4cc`](#insn-00bfa4cc)

~~~json
{
  "source": "00bfa4cc",
  "target": "00c5b6b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa4d4`](#insn-00bfa4d4)

~~~json
{
  "source": "00bfa4d4",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa4dc`](#insn-00bfa4dc)

~~~json
{
  "source": "00bfa4dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa4e0`](#insn-00bfa4e0)

~~~json
{
  "source": "00bfa4e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa4e8`](#insn-00bfa4e8)

~~~json
{
  "source": "00bfa4e8",
  "target": "00c57e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa4f0`](#insn-00bfa4f0)

~~~json
{
  "source": "00bfa4f0",
  "target": "002b179e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b179e",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6d75746578206c6f636b206661696c656400",
  "capture_start": "002b179e",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfa4f4`](#insn-00bfa4f4)

~~~json
{
  "source": "00bfa4f4",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
