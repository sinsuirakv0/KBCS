# 006feeac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0060.md#review-7c72c8a0900d2bd5062f11f45a37ac5e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0021.md#review-7c72c8a0900d2bd5062f11f45a37ac5e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006feeac",
  "name": "FUN_006feeac",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b425710763e212af9fa75101b9204ac0ac4c51ac9912187fcf730aaecfc92ba",
  "source_text_sha256": "7b425710763e212af9fa75101b9204ac0ac4c51ac9912187fcf730aaecfc92ba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006feeac",
        "006fef6b"
      ]
    ],
    "bytes_sha256": "12c6e22dd54c7e48eba7310d99459be6325fead14ece88b35c9812aa83fb83b2",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006b7130](../006b7/006b7130.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 709 bytes

~~~c

void FUN_006feeac(undefined8 param_1,char *param_2)

{
  char cVar1;
  long lVar2;
  
  cVar1 = *param_2;
  lVar2 = FUN_008514f8();
  if (cVar1 == '\0') {
    FUN_008514f8();
    FUN_006b7130(lVar2 + 0x42ef60,0,0,1);
  }
  else {
                    /* try { // try from 006feed4 to 007fef2f has its CatchHandler @ 00704bfc */
    if (0.0 < *(double *)(BYTE_ARRAY_0042ef4d + lVar2 + 0x23)) {
      lVar2 = FUN_008514f8();
      FUN_008514f8();
      FUN_006b7130(lVar2 + 0x42ef60,0,1,1);
    }
    lVar2 = FUN_008514f8();
    if (*(double *)((long)&DWORD_0042ef78 + lVar2) <= 0.0) {
      return;
    }
  }
  lVar2 = FUN_008514f8();
  FUN_008514f8();
  FUN_006b7130(lVar2 + 0x42ef60,1,cVar1,1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006feeac"></a> `006feeac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006feeb0"></a> `006feeb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006feeb4"></a> `006feeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006feeb8"></a> `006feeb8` | `33 00 40 39` | ldrb w19,[x1] | `FALL_THROUGH`
<a id="insn-006feebc"></a> `006feebc` | `8f 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006feec0"></a> `006feec0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006feec4"></a> `006feec4` | `13 03 00 34` | cbz w19,0x006fef24 | `CONDITIONAL_JUMP`
<a id="insn-006feec8"></a> `006feec8` | `08 ee 9d 52` | mov w8,#0xef70 | `FALL_THROUGH`
<a id="insn-006feecc"></a> `006feecc` | `48 08 a0 72` | movk w8,#0x42, LSL #16 | `FALL_THROUGH`
<a id="insn-006feed0"></a> `006feed0` | `80 6a 68 fc` | ldr d0,[x20,x8] | `FALL_THROUGH`
<a id="insn-006feed4"></a> `006feed4` | `08 20 60 1e` | fcmp d0,#0.0 | `FALL_THROUGH`
<a id="insn-006feed8"></a> `006feed8` | `4d 01 00 54` | b.le 0x006fef00 | `CONDITIONAL_JUMP`
<a id="insn-006feedc"></a> `006feedc` | `87 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006feee0"></a> `006feee0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006feee4"></a> `006feee4` | `85 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006feee8"></a> `006feee8` | `88 ba 50 91` | add x8,x20,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-006feeec"></a> `006feeec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006feef0"></a> `006feef0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-006feef4"></a> `006feef4` | `00 81 3d 91` | add x0,x8,#0xf60 | `FALL_THROUGH`
<a id="insn-006feef8"></a> `006feef8` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-006feefc"></a> `006feefc` | `8d e0 fe 97` | bl 0x006b7130 | `UNCONDITIONAL_CALL`
<a id="insn-006fef00"></a> `006fef00` | `7e 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fef04"></a> `006fef04` | `08 ef 9d 52` | mov w8,#0xef78 | `FALL_THROUGH`
<a id="insn-006fef08"></a> `006fef08` | `48 08 a0 72` | movk w8,#0x42, LSL #16 | `FALL_THROUGH`
<a id="insn-006fef0c"></a> `006fef0c` | `00 68 68 fc` | ldr d0,[x0,x8] | `FALL_THROUGH`
<a id="insn-006fef10"></a> `006fef10` | `08 20 60 1e` | fcmp d0,#0.0 | `FALL_THROUGH`
<a id="insn-006fef14"></a> `006fef14` | `6c 01 00 54` | b.gt 0x006fef40 | `CONDITIONAL_JUMP`
<a id="insn-006fef18"></a> `006fef18` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fef1c"></a> `006fef1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fef20"></a> `006fef20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006fef24"></a> `006fef24` | `75 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fef28"></a> `006fef28` | `88 ba 50 91` | add x8,x20,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-006fef2c"></a> `006fef2c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006fef30"></a> `006fef30` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-006fef34"></a> `006fef34` | `00 81 3d 91` | add x0,x8,#0xf60 | `FALL_THROUGH`
<a id="insn-006fef38"></a> `006fef38` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-006fef3c"></a> `006fef3c` | `7d e0 fe 97` | bl 0x006b7130 | `UNCONDITIONAL_CALL`
<a id="insn-006fef40"></a> `006fef40` | `6e 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fef44"></a> `006fef44` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006fef48"></a> `006fef48` | `6c 49 05 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006fef4c"></a> `006fef4c` | `88 ba 50 91` | add x8,x20,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-006fef50"></a> `006fef50` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006fef54"></a> `006fef54` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-006fef58"></a> `006fef58` | `00 81 3d 91` | add x0,x8,#0xf60 | `FALL_THROUGH`
<a id="insn-006fef5c"></a> `006fef5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-006fef60"></a> `006fef60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fef64"></a> `006fef64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fef68"></a> `006fef68` | `72 e0 fe 17` | b 0x006b7130 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006feeac`](#insn-006feeac) 範囲 `[['006feeac', '006feec7']]`
  - `CONDITIONAL_JUMP` [`006feec4`](#insn-006feec4) → [`006fef24`](#insn-006fef24)
  - `FALL_THROUGH` [`006feec4`](#insn-006feec4) → [`006feec8`](#insn-006feec8)
- ブロック [`006feec8`](#insn-006feec8) 範囲 `[['006feec8', '006feed3']]`
  - `FALL_THROUGH` [`006feed0`](#insn-006feed0) → [`006feed4`](#insn-006feed4)
- ブロック [`006feed4`](#insn-006feed4) 範囲 `[['006feed4', '006feedb']]`
  - `CONDITIONAL_JUMP` [`006feed8`](#insn-006feed8) → [`006fef00`](#insn-006fef00)
  - `FALL_THROUGH` [`006feed8`](#insn-006feed8) → [`006feedc`](#insn-006feedc)
- ブロック [`006feedc`](#insn-006feedc) 範囲 `[['006feedc', '006feeff']]`
  - `FALL_THROUGH` [`006feefc`](#insn-006feefc) → [`006fef00`](#insn-006fef00)
- ブロック [`006fef00`](#insn-006fef00) 範囲 `[['006fef00', '006fef17']]`
  - `CONDITIONAL_JUMP` [`006fef14`](#insn-006fef14) → [`006fef40`](#insn-006fef40)
  - `FALL_THROUGH` [`006fef14`](#insn-006fef14) → [`006fef18`](#insn-006fef18)
- ブロック [`006fef18`](#insn-006fef18) 範囲 `[['006fef18', '006fef23']]`
- ブロック [`006fef24`](#insn-006fef24) 範囲 `[['006fef24', '006fef3f']]`
  - `FALL_THROUGH` [`006fef3c`](#insn-006fef3c) → [`006fef40`](#insn-006fef40)
- ブロック [`006fef40`](#insn-006fef40) 範囲 `[['006fef40', '006fef6b']]`

## 命令位置別の参照

- [`006feeac`](#insn-006feeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006feeb0`](#insn-006feeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006feebc`](#insn-006feebc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006feec4`](#insn-006feec4) → [`006fef24`](#insn-006fef24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006feed0`](#insn-006feed0) → `0042ef70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`006feed8`](#insn-006feed8) → [`006fef00`](#insn-006fef00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006feedc`](#insn-006feedc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006feee4`](#insn-006feee4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006feefc`](#insn-006feefc) → [`006b7130`](../006b7/006b7130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b7130` · 推定シンボル `None` · 推定型 `None`
- [`006fef00`](#insn-006fef00) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fef0c`](#insn-006fef0c) → `0042ef78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`006fef14`](#insn-006fef14) → [`006fef40`](#insn-006fef40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fef18`](#insn-006fef18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fef1c`](#insn-006fef1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fef24`](#insn-006fef24) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fef3c`](#insn-006fef3c) → [`006b7130`](../006b7/006b7130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b7130` · 推定シンボル `None` · 推定型 `None`
- [`006fef40`](#insn-006fef40) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fef48`](#insn-006fef48) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006fef60`](#insn-006fef60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fef64`](#insn-006fef64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fef68`](#insn-006fef68) → [`006b7130`](../006b7/006b7130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b7130` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006feeac`](#insn-006feeac)

~~~json
{
  "source": "006feeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006feeb0`](#insn-006feeb0)

~~~json
{
  "source": "006feeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006feebc`](#insn-006feebc)

~~~json
{
  "source": "006feebc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006feec4`](#insn-006feec4)

~~~json
{
  "source": "006feec4",
  "target": "006fef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006feed0`](#insn-006feed0)

~~~json
{
  "source": "006feed0",
  "target": "0042ef70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef4d",
  "offset": 35,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440ed001500c1d309302940495089e0a9d0c0a0300020c1fd001500e00d3d4d5",
  "capture_start": "0042ef4d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006feed8`](#insn-006feed8)

~~~json
{
  "source": "006feed8",
  "target": "006fef00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006feedc`](#insn-006feedc)

~~~json
{
  "source": "006feedc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006feee4`](#insn-006feee4)

~~~json
{
  "source": "006feee4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006feefc`](#insn-006feefc)

~~~json
{
  "source": "006feefc",
  "target": "006b7130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef00`](#insn-006fef00)

~~~json
{
  "source": "006fef00",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef0c`](#insn-006fef0c)

~~~json
{
  "source": "006fef0c",
  "target": "0042ef78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef78",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "d4880400",
  "capture_start": "0042ef78",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006fef14`](#insn-006fef14)

~~~json
{
  "source": "006fef14",
  "target": "006fef40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fef18`](#insn-006fef18)

~~~json
{
  "source": "006fef18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fef1c`](#insn-006fef1c)

~~~json
{
  "source": "006fef1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fef24`](#insn-006fef24)

~~~json
{
  "source": "006fef24",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef3c`](#insn-006fef3c)

~~~json
{
  "source": "006fef3c",
  "target": "006b7130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef40`](#insn-006fef40)

~~~json
{
  "source": "006fef40",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef48`](#insn-006fef48)

~~~json
{
  "source": "006fef48",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fef60`](#insn-006fef60)

~~~json
{
  "source": "006fef60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fef64`](#insn-006fef64)

~~~json
{
  "source": "006fef64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fef68`](#insn-006fef68)

~~~json
{
  "source": "006fef68",
  "target": "006b7130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
