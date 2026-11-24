# 00bb6ebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb6a94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-7bf8adb6e343ec67eb98b15aa836e109)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb6f58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-cb90b704b7451d6f5f73a6e889a2369d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6ebc",
  "name": "_ZN8firebase9messaging16PollableListenerD0Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8",
  "source_text_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb6ebc",
        "00bb6f0b"
      ]
    ],
    "bytes_sha256": "c17838e2f506880e628d1907e4bbd459888fad3d59db6d557f7ed2a723f23c75",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aac0](../00c5a/00c5aac0.md)
- [00c5d380](../00c5d/00c5d380.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 397 bytes

~~~c

void _ZN8firebase9messaging16PollableListenerD0Ev(long *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[1];
  *param_1 = (long)(PTR__ZTVN8firebase9messaging16PollableListenerE_00c9b900 + 0x10);
  if (__ptr != (void *)0x0) {
    _ZN8firebase9messaging20PollableListenerImplD2Ev(__ptr);
    _ZdlPv(__ptr);
  }
  _ZN8firebase9messaging8ListenerD2Ev(param_1);
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb6ebc"></a> `00bb6ebc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb6ec0"></a> `00bb6ec0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6ec4"></a> `00bb6ec4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bb6ec8"></a> `00bb6ec8` | `28 07 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bb6ecc"></a> `00bb6ecc` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bb6ed0"></a> `00bb6ed0` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bb6ed4"></a> `00bb6ed4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb6ed8"></a> `00bb6ed8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bb6edc"></a> `00bb6edc` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bb6ee0"></a> `00bb6ee0` | `b4 00 00 b4` | cbz x20,0x00bb6ef4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6ee4"></a> `00bb6ee4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bb6ee8"></a> `00bb6ee8` | `26 99 02 94` | bl 0x00c5d380 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6eec"></a> `00bb6eec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bb6ef0"></a> `00bb6ef0` | `f0 83 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6ef4"></a> `00bb6ef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6ef8"></a> `00bb6ef8` | `f2 8e 02 94` | bl 0x00c5aac0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6efc"></a> `00bb6efc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6f00"></a> `00bb6f00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6f04"></a> `00bb6f04` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb6f08"></a> `00bb6f08` | `ea 83 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb6ebc`](#insn-00bb6ebc) 範囲 `[['00bb6ebc', '00bb6ee3']]`
  - `CONDITIONAL_JUMP` [`00bb6ee0`](#insn-00bb6ee0) → [`00bb6ef4`](#insn-00bb6ef4)
  - `FALL_THROUGH` [`00bb6ee0`](#insn-00bb6ee0) → [`00bb6ee4`](#insn-00bb6ee4)
- ブロック [`00bb6ee4`](#insn-00bb6ee4) 範囲 `[['00bb6ee4', '00bb6ef3']]`
  - `FALL_THROUGH` [`00bb6ef0`](#insn-00bb6ef0) → [`00bb6ef4`](#insn-00bb6ef4)
- ブロック [`00bb6ef4`](#insn-00bb6ef4) 範囲 `[['00bb6ef4', '00bb6f0b']]`

## 命令位置別の参照

- [`00bb6ebc`](#insn-00bb6ebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ec0`](#insn-00bb6ec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ed0`](#insn-00bb6ed0) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb6edc`](#insn-00bb6edc) → `00c91228`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00bb6ee0`](#insn-00bb6ee0) → [`00bb6ef4`](#insn-00bb6ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ee8`](#insn-00bb6ee8) → [`00c5d380`](../00c5d/00c5d380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d380` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ef0`](#insn-00bb6ef0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ef8`](#insn-00bb6ef8) → [`00c5aac0`](../00c5a/00c5aac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aac0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6efc`](#insn-00bb6efc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6f08`](#insn-00bb6f08) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb6ebc`](#insn-00bb6ebc)

~~~json
{
  "source": "00bb6ebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6ec0`](#insn-00bb6ec0)

~~~json
{
  "source": "00bb6ec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6ed0`](#insn-00bb6ed0)

~~~json
{
  "source": "00bb6ed0",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb6edc`](#insn-00bb6edc)

~~~json
{
  "source": "00bb6edc",
  "target": "00c91228",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91218",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bb6ee0`](#insn-00bb6ee0)

~~~json
{
  "source": "00bb6ee0",
  "target": "00bb6ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6ee8`](#insn-00bb6ee8)

~~~json
{
  "source": "00bb6ee8",
  "target": "00c5d380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6ef0`](#insn-00bb6ef0)

~~~json
{
  "source": "00bb6ef0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6ef8`](#insn-00bb6ef8)

~~~json
{
  "source": "00bb6ef8",
  "target": "00c5aac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6efc`](#insn-00bb6efc)

~~~json
{
  "source": "00bb6efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6f08`](#insn-00bb6f08)

~~~json
{
  "source": "00bb6f08",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
