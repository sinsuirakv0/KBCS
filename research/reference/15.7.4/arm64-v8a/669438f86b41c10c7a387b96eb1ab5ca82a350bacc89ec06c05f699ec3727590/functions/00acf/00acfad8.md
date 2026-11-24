# 00acfad8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfa94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-7ea5f5dfa073704bf5aae6dbfcb38a54)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2f590`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-c604b4db26450fca8672e677e2fc1210)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfad8",
  "name": "FUN_00acfad8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "905df1cef6b353b8dfe03748090259438697144471b685adbb05bc2beb942f7b",
  "source_text_sha256": "905df1cef6b353b8dfe03748090259438697144471b685adbb05bc2beb942f7b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfad8",
        "00acfb2b"
      ]
    ],
    "bytes_sha256": "75ca2cd5f1d3f55ee452f063fa62b97d867f9f60e5b9f865ef6d1498086c4bc1",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0058b674](../0058b/0058b674.md)
- [005d8f58](../005d8/005d8f58.md)
- [00617dec](../00617/00617dec.md)
- [00624a0c](../00624/00624a0c.md)
- [0062da7c](../0062d/0062da7c.md)
- [0063eb28](../0063e/0063eb28.md)
- [00680234](../00680/00680234.md)
- [00680a7c](../00680/00680a7c.md)
- [006a7120](../006a7/006a7120.md)
- [006aef04](../006ae/006aef04.md)
- [006d6d04](../006d6/006d6d04.md)
- [0072f3c8](../0072f/0072f3c8.md)
- [00730204](../00730/00730204.md)
- [00733374](../00733/00733374.md)
- [0088f740](../0088f/0088f740.md)
- [008a76c0](../008a7/008a76c0.md)
- [008b9174](../008b9/008b9174.md)
- [008be650](../008be/008be650.md)
- [0092bc08](../0092b/0092bc08.md)
- [0092d380](../0092d/0092d380.md)
- [0094f64c](../0094f/0094f64c.md)
- [0094f7d0](../0094f/0094f7d0.md)
- [00957320](../00957/00957320.md)
- [00957f9c](../00957/00957f9c.md)
- [009613bc](../00961/009613bc.md)
- [00963004](../00963/00963004.md)
- [00a26d00](../00a26/00a26d00.md)
- [00a2720c](../00a27/00a2720c.md)
- [00a28684](../00a28/00a28684.md)
- [00a28788](../00a28/00a28788.md)
- [00a7268c](../00a72/00a7268c.md)
- [00a788d0](../00a78/00a788d0.md)
- [00a823d8](../00a82/00a823d8.md)

## 呼び出し先

- [00adc094](../00adc/00adc094.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 356 bytes

~~~c

int FUN_00acfad8(undefined8 param_1)

{
  uint uVar1;
  uint uVar2;
  undefined8 uVar3;
  
  uVar3 = FUN_00adc094();
  uVar1 = 50000;
  if ((uint)uVar3 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar3 >> 0x10) & 0xffff;
  }
  uVar2 = FUN_00adc094(param_1);
  uVar2 = uVar2 & 0xffff;
  if (49999 < uVar2) {
    uVar2 = 50000;
  }
  return uVar2 + uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfad8"></a> `00acfad8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acfadc"></a> `00acfadc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfae0"></a> `00acfae0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfae4"></a> `00acfae4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acfae8"></a> `00acfae8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acfaec"></a> `00acfaec` | `6a 31 00 94` | bl 0x00adc094 | `UNCONDITIONAL_CALL`
<a id="insn-00acfaf0"></a> `00acfaf0` | `e8 95 a7 12` | mov w8,#0xc350ffff | `FALL_THROUGH`
<a id="insn-00acfaf4"></a> `00acfaf4` | `09 7c 10 53` | lsr w9,w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acfaf8"></a> `00acfaf8` | `14 6a 98 52` | mov w20,#0xc350 | `FALL_THROUGH`
<a id="insn-00acfafc"></a> `00acfafc` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00acfb00"></a> `00acfb00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acfb04"></a> `00acfb04` | `95 82 89 1a` | csel w21,w20,w9,hi | `FALL_THROUGH`
<a id="insn-00acfb08"></a> `00acfb08` | `63 31 00 94` | bl 0x00adc094 | `UNCONDITIONAL_CALL`
<a id="insn-00acfb0c"></a> `00acfb0c` | `08 3c 00 12` | and w8,w0,#0xffff | `FALL_THROUGH`
<a id="insn-00acfb10"></a> `00acfb10` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00acfb14"></a> `00acfb14` | `08 31 94 1a` | csel w8,w8,w20,cc | `FALL_THROUGH`
<a id="insn-00acfb18"></a> `00acfb18` | `00 01 15 0b` | add w0,w8,w21 | `FALL_THROUGH`
<a id="insn-00acfb1c"></a> `00acfb1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfb20"></a> `00acfb20` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfb24"></a> `00acfb24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acfb28"></a> `00acfb28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfad8`](#insn-00acfad8) 範囲 `[['00acfad8', '00acfb2b']]`

## 命令位置別の参照

- [`00acfad8`](#insn-00acfad8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfadc`](#insn-00acfadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfae0`](#insn-00acfae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfaec`](#insn-00acfaec) → [`00adc094`](../00adc/00adc094.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc094` · 推定シンボル `None` · 推定型 `None`
- [`00acfb08`](#insn-00acfb08) → [`00adc094`](../00adc/00adc094.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc094` · 推定シンボル `None` · 推定型 `None`
- [`00acfb1c`](#insn-00acfb1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb20`](#insn-00acfb20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfb24`](#insn-00acfb24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfad8`](#insn-00acfad8)

~~~json
{
  "source": "00acfad8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfadc`](#insn-00acfadc)

~~~json
{
  "source": "00acfadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfae0`](#insn-00acfae0)

~~~json
{
  "source": "00acfae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfaec`](#insn-00acfaec)

~~~json
{
  "source": "00acfaec",
  "target": "00adc094",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb08`](#insn-00acfb08)

~~~json
{
  "source": "00acfb08",
  "target": "00adc094",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfb1c`](#insn-00acfb1c)

~~~json
{
  "source": "00acfb1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb20`](#insn-00acfb20)

~~~json
{
  "source": "00acfb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfb24`](#insn-00acfb24)

~~~json
{
  "source": "00acfb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
