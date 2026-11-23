# 00acf9cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfa94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-46d4e391faec96e19103e860b38d7b8b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acf9cc",
  "name": "FUN_00acf9cc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b0654c2539a2beda08f3ad4616569142a65c919842ebb76bd7091fbd3644bcd",
  "source_text_sha256": "9b0654c2539a2beda08f3ad4616569142a65c919842ebb76bd7091fbd3644bcd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acf9cc",
        "00acfa1f"
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
- [00a26cbc](../00a26/00a26cbc.md)
- [00a271c8](../00a27/00a271c8.md)
- [00a28640](../00a28/00a28640.md)
- [00a28744](../00a28/00a28744.md)
- [00a72648](../00a72/00a72648.md)
- [00a7888c](../00a78/00a7888c.md)
- [00a82394](../00a82/00a82394.md)

## 呼び出し先

- [00adbf88](../00adb/00adbf88.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 356 bytes

~~~c

int FUN_00acf9cc(undefined8 param_1)

{
  uint uVar1;
  uint uVar2;
  undefined8 uVar3;
  
  uVar3 = FUN_00adbf88();
  uVar1 = 50000;
  if ((uint)uVar3 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar3 >> 0x10) & 0xffff;
  }
  uVar2 = FUN_00adbf88(param_1);
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
<a id="insn-00acf9cc"></a> `00acf9cc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acf9d0"></a> `00acf9d0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf9d4"></a> `00acf9d4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf9d8"></a> `00acf9d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acf9dc"></a> `00acf9dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acf9e0"></a> `00acf9e0` | `6a 31 00 94` | bl 0x00adbf88 | `UNCONDITIONAL_CALL`
<a id="insn-00acf9e4"></a> `00acf9e4` | `e8 95 a7 12` | mov w8,#0xc350ffff | `FALL_THROUGH`
<a id="insn-00acf9e8"></a> `00acf9e8` | `09 7c 10 53` | lsr w9,w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acf9ec"></a> `00acf9ec` | `14 6a 98 52` | mov w20,#0xc350 | `FALL_THROUGH`
<a id="insn-00acf9f0"></a> `00acf9f0` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00acf9f4"></a> `00acf9f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf9f8"></a> `00acf9f8` | `95 82 89 1a` | csel w21,w20,w9,hi | `FALL_THROUGH`
<a id="insn-00acf9fc"></a> `00acf9fc` | `63 31 00 94` | bl 0x00adbf88 | `UNCONDITIONAL_CALL`
<a id="insn-00acfa00"></a> `00acfa00` | `08 3c 00 12` | and w8,w0,#0xffff | `FALL_THROUGH`
<a id="insn-00acfa04"></a> `00acfa04` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00acfa08"></a> `00acfa08` | `08 31 94 1a` | csel w8,w8,w20,cc | `FALL_THROUGH`
<a id="insn-00acfa0c"></a> `00acfa0c` | `00 01 15 0b` | add w0,w8,w21 | `FALL_THROUGH`
<a id="insn-00acfa10"></a> `00acfa10` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfa14"></a> `00acfa14` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfa18"></a> `00acfa18` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acfa1c"></a> `00acfa1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acf9cc`](#insn-00acf9cc) 範囲 `[['00acf9cc', '00acfa1f']]`

## 命令位置別の参照

- [`00acf9cc`](#insn-00acf9cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf9d0`](#insn-00acf9d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf9d4`](#insn-00acf9d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf9e0`](#insn-00acf9e0) → [`00adbf88`](../00adb/00adbf88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adbf88` · 推定シンボル `None` · 推定型 `None`
- [`00acf9fc`](#insn-00acf9fc) → [`00adbf88`](../00adb/00adbf88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adbf88` · 推定シンボル `None` · 推定型 `None`
- [`00acfa10`](#insn-00acfa10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfa14`](#insn-00acfa14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfa18`](#insn-00acfa18) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acf9cc`](#insn-00acf9cc)

~~~json
{
  "source": "00acf9cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf9d0`](#insn-00acf9d0)

~~~json
{
  "source": "00acf9d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf9d4`](#insn-00acf9d4)

~~~json
{
  "source": "00acf9d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf9e0`](#insn-00acf9e0)

~~~json
{
  "source": "00acf9e0",
  "target": "00adbf88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf9fc`](#insn-00acf9fc)

~~~json
{
  "source": "00acf9fc",
  "target": "00adbf88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfa10`](#insn-00acfa10)

~~~json
{
  "source": "00acfa10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfa14`](#insn-00acfa14)

~~~json
{
  "source": "00acfa14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfa18`](#insn-00acfa18)

~~~json
{
  "source": "00acfa18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
