# 00bdf6ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdf2c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf2c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-fcc5ddfdf3dd8b819a0fd3fbb6c016a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdf788`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-087dc3fb32f29a993e55d4f3f208c271)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf6ec",
  "name": "_ZN8firebase4auth22AndroidWrappedUserInfoD2Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a798447537e403e0f3331058f17a37c65f7d3420924ea3aae838f6ef1829a0d",
  "source_text_sha256": "3a798447537e403e0f3331058f17a37c65f7d3420924ea3aae838f6ef1829a0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf6ec",
        "00bdf73b"
      ]
    ],
    "bytes_sha256": "99a6693755e900daea03b0eb1bcd1079d0f3711f75176584d9183e4c780dc7e8",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b080](../00c5b/00c5b080.md)
- [00c5db80](../00c5d/00c5db80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 398 bytes

~~~c

void _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev(long *param_1)

{
  long *plVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9ba60 + 0x10);
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)param_1[0x13]);
  (**(code **)(*plVar1 + 0xb0))(plVar1,param_1[0x14]);
  param_1[0x14] = 0;
  _ZN8firebase4auth17UserInfoInterfaceD2Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf6ec"></a> `00bdf6ec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdf6f0"></a> `00bdf6f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf6f4"></a> `00bdf6f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdf6f8"></a> `00bdf6f8` | `e9 05 00 90` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdf6fc"></a> `00bdf6fc` | `08 4c 40 f9` | ldr x8,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf700"></a> `00bdf700` | `29 31 45 f9` | ldr x9,[x9, #0xa60] | `FALL_THROUGH`
<a id="insn-00bdf704"></a> `00bdf704` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdf708"></a> `00bdf708` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdf70c"></a> `00bdf70c` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bdf710"></a> `00bdf710` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdf714"></a> `00bdf714` | `5b ee 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf718"></a> `00bdf718` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdf71c"></a> `00bdf71c` | `61 52 40 f9` | ldr x1,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdf720"></a> `00bdf720` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf724"></a> `00bdf724` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf728"></a> `00bdf728` | `7f 52 00 f9` | str xzr,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdf72c"></a> `00bdf72c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf730"></a> `00bdf730` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf734"></a> `00bdf734` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdf738"></a> `00bdf738` | `12 f9 01 14` | b 0x00c5db80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf6ec`](#insn-00bdf6ec) 範囲 `[['00bdf6ec', '00bdf73b']]`

## 命令位置別の参照

- [`00bdf6ec`](#insn-00bdf6ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf6f0`](#insn-00bdf6f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf700`](#insn-00bdf700) → `00c9ba60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdf70c`](#insn-00bdf70c) → `00c92910`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdf714`](#insn-00bdf714) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdf72c`](#insn-00bdf72c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf738`](#insn-00bdf738) → [`00c5db80`](../00c5d/00c5db80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf6ec`](#insn-00bdf6ec)

~~~json
{
  "source": "00bdf6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf6f0`](#insn-00bdf6f0)

~~~json
{
  "source": "00bdf6f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf700`](#insn-00bdf700)

~~~json
{
  "source": "00bdf700",
  "target": "00c9ba60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdf70c`](#insn-00bdf70c)

~~~json
{
  "source": "00bdf70c",
  "target": "00c92910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92900",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdf714`](#insn-00bdf714)

~~~json
{
  "source": "00bdf714",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf72c`](#insn-00bdf72c)

~~~json
{
  "source": "00bdf72c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf738`](#insn-00bdf738)

~~~json
{
  "source": "00bdf738",
  "target": "00c5db80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
