# 00bba6fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb9708`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9708.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-d7a4c1f61cbca299d5f815ba754238bc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba6fc",
  "name": "_ZN8firebase9messaging10FileLocker11AcquireLockEPKc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79a43928de3cc6f8190f49faebf61e694b1d9f21c7cec90c40fb2935cfeed4d3",
  "source_text_sha256": "79a43928de3cc6f8190f49faebf61e694b1d9f21c7cec90c40fb2935cfeed4d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba6fc",
        "00bba777"
      ]
    ],
    "bytes_sha256": "47b1f3388f2b66350b2a3c4638acfccb3d6f075f8d2181ca5c967fb36909b689",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e620](../00c5e/00c5e620.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bc10](../00c5b/00c5bc10.md)
- [00c5e680](../00c5e/00c5e680.md)
- [00c5e6b0](../00c5e/00c5e6b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 397 bytes

~~~c

int _ZN8firebase9messaging10FileLocker11AcquireLockEPKc(char *param_1)

{
  undefined4 uVar1;
  int __fd;
  int iVar2;
  
  if (DAT_01127418 != 0) {
    _ZN8firebase5Mutex7AcquireEv(DAT_01127418);
  }
  uVar1 = __umask_chk(0);
  __fd = open(param_1,0x42,0x1b6);
  __umask_chk(uVar1);
  if ((__fd < 0) || (iVar2 = flock(__fd,2), iVar2 < 0)) {
    close(__fd);
    __fd = -1;
  }
  return __fd;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba6fc"></a> `00bba6fc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bba700"></a> `00bba700` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba704"></a> `00bba704` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bba708"></a> `00bba708` | `68 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bba70c"></a> `00bba70c` | `08 0d 42 f9` | ldr x8,[x8, #0x418] | `FALL_THROUGH`
<a id="insn-00bba710"></a> `00bba710` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bba714"></a> `00bba714` | `68 00 00 b4` | cbz x8,0x00bba720 | `CONDITIONAL_JUMP`
<a id="insn-00bba718"></a> `00bba718` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bba71c"></a> `00bba71c` | `e1 84 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba720"></a> `00bba720` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bba724"></a> `00bba724` | `3b 85 02 94` | bl 0x00c5bc10 | `UNCONDITIONAL_CALL`
<a id="insn-00bba728"></a> `00bba728` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bba72c"></a> `00bba72c` | `41 08 80 52` | mov w1,#0x42 | `FALL_THROUGH`
<a id="insn-00bba730"></a> `00bba730` | `c2 36 80 52` | mov w2,#0x1b6 | `FALL_THROUGH`
<a id="insn-00bba734"></a> `00bba734` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bba738"></a> `00bba738` | `de 8f 02 94` | bl 0x00c5e6b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bba73c"></a> `00bba73c` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bba740"></a> `00bba740` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bba744"></a> `00bba744` | `33 85 02 94` | bl 0x00c5bc10 | `UNCONDITIONAL_CALL`
<a id="insn-00bba748"></a> `00bba748` | `b3 00 f8 37` | tbnz w19,#0x1f,0x00bba75c | `CONDITIONAL_JUMP`
<a id="insn-00bba74c"></a> `00bba74c` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00bba750"></a> `00bba750` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bba754"></a> `00bba754` | `cb 8f 02 94` | bl 0x00c5e680 | `UNCONDITIONAL_CALL`
<a id="insn-00bba758"></a> `00bba758` | `80 00 f8 36` | tbz w0,#0x1f,0x00bba768 | `CONDITIONAL_JUMP`
<a id="insn-00bba75c"></a> `00bba75c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bba760"></a> `00bba760` | `44 80 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bba764"></a> `00bba764` | `13 00 80 12` | mov w19,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bba768"></a> `00bba768` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bba76c"></a> `00bba76c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bba770"></a> `00bba770` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bba774"></a> `00bba774` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba6fc`](#insn-00bba6fc) 範囲 `[['00bba6fc', '00bba717']]`
  - `CONDITIONAL_JUMP` [`00bba714`](#insn-00bba714) → [`00bba720`](#insn-00bba720)
  - `FALL_THROUGH` [`00bba714`](#insn-00bba714) → [`00bba718`](#insn-00bba718)
- ブロック [`00bba718`](#insn-00bba718) 範囲 `[['00bba718', '00bba71f']]`
  - `FALL_THROUGH` [`00bba71c`](#insn-00bba71c) → [`00bba720`](#insn-00bba720)
- ブロック [`00bba720`](#insn-00bba720) 範囲 `[['00bba720', '00bba74b']]`
  - `CONDITIONAL_JUMP` [`00bba748`](#insn-00bba748) → [`00bba75c`](#insn-00bba75c)
  - `FALL_THROUGH` [`00bba748`](#insn-00bba748) → [`00bba74c`](#insn-00bba74c)
- ブロック [`00bba74c`](#insn-00bba74c) 範囲 `[['00bba74c', '00bba75b']]`
  - `CONDITIONAL_JUMP` [`00bba758`](#insn-00bba758) → [`00bba768`](#insn-00bba768)
  - `FALL_THROUGH` [`00bba758`](#insn-00bba758) → [`00bba75c`](#insn-00bba75c)
- ブロック [`00bba75c`](#insn-00bba75c) 範囲 `[['00bba75c', '00bba767']]`
  - `FALL_THROUGH` [`00bba764`](#insn-00bba764) → [`00bba768`](#insn-00bba768)
- ブロック [`00bba768`](#insn-00bba768) 範囲 `[['00bba768', '00bba777']]`

## 命令位置別の参照

- [`00bba6fc`](#insn-00bba6fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba700`](#insn-00bba700) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba70c`](#insn-00bba70c) → `01127418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bba714`](#insn-00bba714) → [`00bba720`](#insn-00bba720) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba71c`](#insn-00bba71c) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bba724`](#insn-00bba724) → [`00c5bc10`](../00c5b/00c5bc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc10` · 推定シンボル `None` · 推定型 `None`
- [`00bba738`](#insn-00bba738) → [`00c5e6b0`](../00c5e/00c5e6b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e6b0` · 推定シンボル `None` · 推定型 `None`
- [`00bba744`](#insn-00bba744) → [`00c5bc10`](../00c5b/00c5bc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc10` · 推定シンボル `None` · 推定型 `None`
- [`00bba748`](#insn-00bba748) → [`00bba75c`](#insn-00bba75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba754`](#insn-00bba754) → [`00c5e680`](../00c5e/00c5e680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e680` · 推定シンボル `None` · 推定型 `None`
- [`00bba758`](#insn-00bba758) → [`00bba768`](#insn-00bba768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba760`](#insn-00bba760) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bba768`](#insn-00bba768) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba6fc`](#insn-00bba6fc)

~~~json
{
  "source": "00bba6fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba700`](#insn-00bba700)

~~~json
{
  "source": "00bba700",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba70c`](#insn-00bba70c)

~~~json
{
  "source": "00bba70c",
  "target": "01127418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bba714`](#insn-00bba714)

~~~json
{
  "source": "00bba714",
  "target": "00bba720",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba71c`](#insn-00bba71c)

~~~json
{
  "source": "00bba71c",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba724`](#insn-00bba724)

~~~json
{
  "source": "00bba724",
  "target": "00c5bc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba738`](#insn-00bba738)

~~~json
{
  "source": "00bba738",
  "target": "00c5e6b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba744`](#insn-00bba744)

~~~json
{
  "source": "00bba744",
  "target": "00c5bc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba748`](#insn-00bba748)

~~~json
{
  "source": "00bba748",
  "target": "00bba75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba754`](#insn-00bba754)

~~~json
{
  "source": "00bba754",
  "target": "00c5e680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba758`](#insn-00bba758)

~~~json
{
  "source": "00bba758",
  "target": "00bba768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba760`](#insn-00bba760)

~~~json
{
  "source": "00bba760",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bba768`](#insn-00bba768)

~~~json
{
  "source": "00bba768",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
