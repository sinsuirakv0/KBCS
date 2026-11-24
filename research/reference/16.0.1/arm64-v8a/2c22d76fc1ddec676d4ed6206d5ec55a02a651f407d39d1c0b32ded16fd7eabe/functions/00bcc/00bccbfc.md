# 00bccbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-cd583bd2b3cdd95ccfeb4e94f236c043)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-1b630de1dbf1878e9399e260b9255282)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccbfc",
  "name": "_ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1986486adf9931b89021e7cdba390b8b2614e2f7fae751946c5cf176c97a209",
  "source_text_sha256": "a1986486adf9931b89021e7cdba390b8b2614e2f7fae751946c5cf176c97a209",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccbfc",
        "00bccc37"
      ]
    ],
    "bytes_sha256": "4e4d66a13b593aaf66e4deb391d12dde00ad7658379e87b375cf79e3572260bb",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 309 bytes

~~~c

undefined8 _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bccc30 to 00cccc3b has its CatchHandler @ 00bce900 */
  return (&DAT_01126800)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccbfc"></a> `00bccbfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccc00"></a> `00bccc00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccc04"></a> `00bccc04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccc08"></a> `00bccc08` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bccc0c"></a> `00bccc0c` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bccc10"></a> `00bccc10` | `8b 00 00 54` | b.lt 0x00bccc20 | `CONDITIONAL_JUMP`
<a id="insn-00bccc14"></a> `00bccc14` | `e0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bccc18"></a> `00bccc18` | `00 9c 0d 91` | add x0,x0,#0x367 | `FALL_THROUGH`
<a id="insn-00bccc1c"></a> `00bccc1c` | `f9 38 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bccc20"></a> `00bccc20` | `c8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccc24"></a> `00bccc24` | `08 01 20 91` | add x8,x8,#0x800 | `FALL_THROUGH`
<a id="insn-00bccc28"></a> `00bccc28` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bccc2c"></a> `00bccc2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccc30"></a> `00bccc30` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccc34"></a> `00bccc34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccbfc`](#insn-00bccbfc) 範囲 `[['00bccbfc', '00bccc13']]`
  - `CONDITIONAL_JUMP` [`00bccc10`](#insn-00bccc10) → [`00bccc20`](#insn-00bccc20)
  - `FALL_THROUGH` [`00bccc10`](#insn-00bccc10) → [`00bccc14`](#insn-00bccc14)
- ブロック [`00bccc14`](#insn-00bccc14) 範囲 `[['00bccc14', '00bccc1f']]`
  - `FALL_THROUGH` [`00bccc1c`](#insn-00bccc1c) → [`00bccc20`](#insn-00bccc20)
- ブロック [`00bccc20`](#insn-00bccc20) 範囲 `[['00bccc20', '00bccc2f']]`
  - `FALL_THROUGH` [`00bccc2c`](#insn-00bccc2c) → [`00bccc30`](#insn-00bccc30)
- ブロック [`00bccc30`](#insn-00bccc30) 範囲 `[['00bccc30', '00bccc37']]`

## 命令位置別の参照

- [`00bccbfc`](#insn-00bccbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc00`](#insn-00bccc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc10`](#insn-00bccc10) → [`00bccc20`](#insn-00bccc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccc18`](#insn-00bccc18) → `002a8367`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccc1c`](#insn-00bccc1c) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bccc28`](#insn-00bccc28) → `01126800`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccc2c`](#insn-00bccc2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccbfc`](#insn-00bccbfc)

~~~json
{
  "source": "00bccbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc00`](#insn-00bccc00)

~~~json
{
  "source": "00bccc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc10`](#insn-00bccc10)

~~~json
{
  "source": "00bccc10",
  "target": "00bccc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccc18`](#insn-00bccc18)

~~~json
{
  "source": "00bccc18",
  "target": "002a8367",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8367",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a8367",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bccc1c`](#insn-00bccc1c)

~~~json
{
  "source": "00bccc1c",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccc28`](#insn-00bccc28)

~~~json
{
  "source": "00bccc28",
  "target": "01126800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126800",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccc2c`](#insn-00bccc2c)

~~~json
{
  "source": "00bccc2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
