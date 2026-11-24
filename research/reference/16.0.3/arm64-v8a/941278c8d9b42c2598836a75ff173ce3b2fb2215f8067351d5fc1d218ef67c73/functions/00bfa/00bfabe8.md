# 00bfabe8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9bf4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9bf4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-a2c5242c36a25690c2c9b861ea11060f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfabe8",
  "name": "_ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "518f45d3fcb72c155ba6331ac3dcd23dc71faa4aff076c77bc87522b7102cb4c",
  "source_text_sha256": "518f45d3fcb72c155ba6331ac3dcd23dc71faa4aff076c77bc87522b7102cb4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfabe8",
        "00bfac3f"
      ]
    ],
    "bytes_sha256": "cddd96a97459bdb0f20646ee4977d1fe7430fa4e703109f876b2aa3c653dec5e",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c595c0](../00c59/00c595c0.md)

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c59180](../00c59/00c59180.md)
- [00c59190](../00c59/00c59190.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 464 bytes

~~~c

void _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE(long *param_1,long param_2)

{
  uint uVar1;
  
  *param_1 = param_2;
  _ZNSt6__ndk15mutex4lockEv(param_2 + 0x18);
  uVar1 = *(uint *)(param_2 + 0x70);
  if ((uVar1 >> 1 & 1) == 0) {
    FUN_00c54d60(1,param_2 + 8);
    *(uint *)(param_2 + 0x70) = uVar1 | 2;
    _ZNSt6__ndk15mutex6unlockEv(param_2 + 0x18);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfabe8"></a> `00bfabe8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfabec"></a> `00bfabec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfabf0"></a> `00bfabf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfabf4"></a> `00bfabf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfabf8"></a> `00bfabf8` | `01 00 00 f9` | str x1,[x0] | `FALL_THROUGH`
<a id="insn-00bfabfc"></a> `00bfabfc` | `20 60 00 91` | add x0,x1,#0x18 | `FALL_THROUGH`
<a id="insn-00bfac00"></a> `00bfac00` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfac04"></a> `00bfac04` | `5f 79 01 94` | bl 0x00c59180 | `UNCONDITIONAL_CALL`
<a id="insn-00bfac08"></a> `00bfac08` | `74 72 40 b9` | ldr w20,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfac0c"></a> `00bfac0c` | `74 01 08 37` | tbnz w20,#0x1,0x00bfac38 | `CONDITIONAL_JUMP`
<a id="insn-00bfac10"></a> `00bfac10` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bfac14"></a> `00bfac14` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac18"></a> `00bfac18` | `52 68 01 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-00bfac1c"></a> `00bfac1c` | `88 02 1f 32` | orr w8,w20,#0x2 | `FALL_THROUGH`
<a id="insn-00bfac20"></a> `00bfac20` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bfac24"></a> `00bfac24` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfac28"></a> `00bfac28` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac2c"></a> `00bfac2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfac30"></a> `00bfac30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfac34"></a> `00bfac34` | `57 79 01 14` | b 0x00c59190 | `CALL_TERMINATOR`
<a id="insn-00bfac38"></a> `00bfac38` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac3c"></a> `00bfac3c` | `7e 7f e1 97` | bl 0x0045aa34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfabe8`](#insn-00bfabe8) 範囲 `[['00bfabe8', '00bfac0f']]`
  - `CONDITIONAL_JUMP` [`00bfac0c`](#insn-00bfac0c) → [`00bfac38`](#insn-00bfac38)
  - `FALL_THROUGH` [`00bfac0c`](#insn-00bfac0c) → [`00bfac10`](#insn-00bfac10)
- ブロック [`00bfac10`](#insn-00bfac10) 範囲 `[['00bfac10', '00bfac37']]`
- ブロック [`00bfac38`](#insn-00bfac38) 範囲 `[['00bfac38', '00bfac3f']]`

## 命令位置別の参照

- [`00bfabec`](#insn-00bfabec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabf0`](#insn-00bfabf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac04`](#insn-00bfac04) → [`00c59180`](../00c59/00c59180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59180` · 推定シンボル `None` · 推定型 `None`
- [`00bfac0c`](#insn-00bfac0c) → [`00bfac38`](#insn-00bfac38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac18`](#insn-00bfac18) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`00bfac28`](#insn-00bfac28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac2c`](#insn-00bfac2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac34`](#insn-00bfac34) → [`00c59190`](../00c59/00c59190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59190` · 推定シンボル `None` · 推定型 `None`
- [`00bfac3c`](#insn-00bfac3c) → [`0045aa34`](../0045a/0045aa34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045aa34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfabec`](#insn-00bfabec)

~~~json
{
  "source": "00bfabec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabf0`](#insn-00bfabf0)

~~~json
{
  "source": "00bfabf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac04`](#insn-00bfac04)

~~~json
{
  "source": "00bfac04",
  "target": "00c59180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac0c`](#insn-00bfac0c)

~~~json
{
  "source": "00bfac0c",
  "target": "00bfac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac18`](#insn-00bfac18)

~~~json
{
  "source": "00bfac18",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac28`](#insn-00bfac28)

~~~json
{
  "source": "00bfac28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac2c`](#insn-00bfac2c)

~~~json
{
  "source": "00bfac2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac34`](#insn-00bfac34)

~~~json
{
  "source": "00bfac34",
  "target": "00c59190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac3c`](#insn-00bfac3c)

~~~json
{
  "source": "00bfac3c",
  "target": "0045aa34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
