# 00acfa4c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfa08`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-1292b421a0502cc6c3359b8eed828515)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2f504`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f504.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-5f6b0e36461a2a411e98255dd91f089b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfa4c",
  "name": "FUN_00acfa4c",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c43125907101778fd059897f3742812b91a35f18aebbfa39270cecc62c27b62",
  "source_text_sha256": "4c43125907101778fd059897f3742812b91a35f18aebbfa39270cecc62c27b62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfa4c",
        "00acfad7"
      ]
    ],
    "bytes_sha256": "f6915881f2f7109bb6377b73d354a9a15fc3bce5dede61d99119905c468287bc",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006e34b0](../006e3/006e34b0.md)
- [0072f020](../0072f/0072f020.md)
- [0092bc08](../0092b/0092bc08.md)
- [0092d380](../0092d/0092d380.md)
- [009a9ce0](../009a9/009a9ce0.md)
- [00add818](../00add/00add818.md)

## 呼び出し先

- [00adc060](../00adc/00adc060.md)
- [00adc094](../00adc/00adc094.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00acfa4c(undefined8 param_1,int param_2)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  undefined8 uVar4;
  
  uVar4 = FUN_00adc094();
  uVar1 = 50000;
  if ((uint)uVar4 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar4 >> 0x10) & 0xffff;
  }
  uVar3 = FUN_00adc094(param_1);
  uVar3 = uVar3 & 0xffff;
  if (49999 < uVar3) {
    uVar3 = 50000;
  }
  uVar2 = 0xc3500000;
  if (uVar1 < 0xc351) {
    uVar2 = uVar1 << 0x10;
  }
  uVar1 = uVar3 + param_2 & ((int)(uVar3 + param_2) >> 0x1f ^ 0xffffffffU);
  if (49999 < uVar1) {
    uVar1 = 50000;
  }
  FUN_00adc060(param_1,uVar1 | uVar2);
  DAT_00c23fb4 = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfa4c"></a> `00acfa4c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acfa50"></a> `00acfa50` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfa54"></a> `00acfa54` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfa58"></a> `00acfa58` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acfa5c"></a> `00acfa5c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acfa60"></a> `00acfa60` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acfa64"></a> `00acfa64` | `8c 31 00 94` | bl 0x00adc094 | `UNCONDITIONAL_CALL`
<a id="insn-00acfa68"></a> `00acfa68` | `e8 95 a7 12` | mov w8,#0xc350ffff | `FALL_THROUGH`
<a id="insn-00acfa6c"></a> `00acfa6c` | `09 7c 10 53` | lsr w9,w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acfa70"></a> `00acfa70` | `15 6a 98 52` | mov w21,#0xc350 | `FALL_THROUGH`
<a id="insn-00acfa74"></a> `00acfa74` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00acfa78"></a> `00acfa78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acfa7c"></a> `00acfa7c` | `b6 82 89 1a` | csel w22,w21,w9,hi | `FALL_THROUGH`
<a id="insn-00acfa80"></a> `00acfa80` | `85 31 00 94` | bl 0x00adc094 | `UNCONDITIONAL_CALL`
<a id="insn-00acfa84"></a> `00acfa84` | `09 3c 00 12` | and w9,w0,#0xffff | `FALL_THROUGH`
<a id="insn-00acfa88"></a> `00acfa88` | `c8 3e 10 53` | lsl w8,w22,#0x10 | `FALL_THROUGH`
<a id="insn-00acfa8c"></a> `00acfa8c` | `0a 6a b8 52` | mov w10,#0xc3500000 | `FALL_THROUGH`
<a id="insn-00acfa90"></a> `00acfa90` | `3f 01 15 6b` | cmp w9,w21 | `FALL_THROUGH`
<a id="insn-00acfa94"></a> `00acfa94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acfa98"></a> `00acfa98` | `29 31 95 1a` | csel w9,w9,w21,cc | `FALL_THROUGH`
<a id="insn-00acfa9c"></a> `00acfa9c` | `df 02 15 6b` | cmp w22,w21 | `FALL_THROUGH`
<a id="insn-00acfaa0"></a> `00acfaa0` | `29 01 13 0b` | add w9,w9,w19 | `FALL_THROUGH`
<a id="insn-00acfaa4"></a> `00acfaa4` | `48 81 88 1a` | csel w8,w10,w8,hi | `FALL_THROUGH`
<a id="insn-00acfaa8"></a> `00acfaa8` | `29 7d a9 0a` | bic w9,w9,w9, ASR #0x1f | `FALL_THROUGH`
<a id="insn-00acfaac"></a> `00acfaac` | `3f 01 15 6b` | cmp w9,w21 | `FALL_THROUGH`
<a id="insn-00acfab0"></a> `00acfab0` | `29 31 95 1a` | csel w9,w9,w21,cc | `FALL_THROUGH`
<a id="insn-00acfab4"></a> `00acfab4` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfab8"></a> `00acfab8` | `6a 31 00 94` | bl 0x00adc060 | `UNCONDITIONAL_CALL`
<a id="insn-00acfabc"></a> `00acfabc` | `a8 0a 00 90` | adrp x8,0xc23000 | `FALL_THROUGH`
<a id="insn-00acfac0"></a> `00acfac0` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acfac4"></a> `00acfac4` | `09 d1 3e 39` | strb w9,[x8, #0xfb4] | `FALL_THROUGH`
<a id="insn-00acfac8"></a> `00acfac8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfacc"></a> `00acfacc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfad0"></a> `00acfad0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acfad4"></a> `00acfad4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfa4c`](#insn-00acfa4c) 範囲 `[['00acfa4c', '00acfad7']]`

## 命令位置別の参照

- [`00acfa4c`](#insn-00acfa4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfa50`](#insn-00acfa50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfa54`](#insn-00acfa54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfa64`](#insn-00acfa64) → [`00adc094`](../00adc/00adc094.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc094` · 推定シンボル `None` · 推定型 `None`
- [`00acfa80`](#insn-00acfa80) → [`00adc094`](../00adc/00adc094.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc094` · 推定シンボル `None` · 推定型 `None`
- [`00acfab8`](#insn-00acfab8) → [`00adc060`](../00adc/00adc060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adc060` · 推定シンボル `None` · 推定型 `None`
- [`00acfac4`](#insn-00acfac4) → `00c23fb4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acfac8`](#insn-00acfac8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfacc`](#insn-00acfacc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfad0`](#insn-00acfad0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfa4c`](#insn-00acfa4c)

~~~json
{
  "source": "00acfa4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfa50`](#insn-00acfa50)

~~~json
{
  "source": "00acfa50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfa54`](#insn-00acfa54)

~~~json
{
  "source": "00acfa54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfa64`](#insn-00acfa64)

~~~json
{
  "source": "00acfa64",
  "target": "00adc094",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfa80`](#insn-00acfa80)

~~~json
{
  "source": "00acfa80",
  "target": "00adc094",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfab8`](#insn-00acfab8)

~~~json
{
  "source": "00acfab8",
  "target": "00adc060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfac4`](#insn-00acfac4)

~~~json
{
  "source": "00acfac4",
  "target": "00c23fb4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c23fb4",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acfac8`](#insn-00acfac8)

~~~json
{
  "source": "00acfac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfacc`](#insn-00acfacc)

~~~json
{
  "source": "00acfacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfad0`](#insn-00acfad0)

~~~json
{
  "source": "00acfad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
