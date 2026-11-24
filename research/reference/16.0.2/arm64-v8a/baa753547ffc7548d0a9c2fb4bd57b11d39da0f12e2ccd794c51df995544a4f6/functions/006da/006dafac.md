# 006dafac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `006daf54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006daf54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0020.md#compare-7fc58c7e9fa31f1a5a33f72a87233cb2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `006db35c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db35c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0017.md#compare-082fb03a3e35e252c70db34280009f9e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dafac",
  "name": "FUN_006dafac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58e928e0352e724c10a3ef22a3109e3c28755cdd1f24e5794c540594f45d530e",
  "source_text_sha256": "58e928e0352e724c10a3ef22a3109e3c28755cdd1f24e5794c540594f45d530e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dafac",
        "006db05f"
      ]
    ],
    "bytes_sha256": "2074551ac8352bc97608deb988727db2d931f351a987d1b3241a2d54284eed37",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006f252c](../006f2/006f252c.md)

## 呼び出し先

- [0046d7f0](../0046d/0046d7f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 657 bytes

~~~c

undefined8 FUN_006dafac(int *param_1,int param_2)

{
  int *piVar1;
  int *piVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  
  if ((*(byte *)(param_1 + 0xe) & 1) != 0) {
    return 0;
  }
  piVar1 = *(int **)(param_1 + 8);
  piVar2 = *(int **)(param_1 + 10);
  iVar3 = *param_1;
  *param_1 = iVar3 + param_2;
  while( true ) {
    if (piVar1 == piVar2) {
      return 0;
    }
    if (((iVar3 < *piVar1) && (*piVar1 <= *param_1)) &&
       (iVar4 = piVar1[1], iVar5 = FUN_0046d7f0(1000), iVar5 < iVar4)) break;
    piVar1 = piVar1 + 2;
  }
  *param_1 = 0;
  param_1[4] = param_1[7];
  *(double *)(param_1 + 2) = (double)(param_1[6] * 0x3c);
  return 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dafac"></a> `006dafac` | `08 e0 40 39` | ldrb w8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-006dafb0"></a> `006dafb0` | `68 00 00 36` | tbz w8,#0x0,0x006dafbc | `CONDITIONAL_JUMP`
<a id="insn-006dafb4"></a> `006dafb4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-006dafb8"></a> `006dafb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006dafbc"></a> `006dafbc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-006dafc0"></a> `006dafc0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dafc4"></a> `006dafc4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dafc8"></a> `006dafc8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dafcc"></a> `006dafcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006dafd0"></a> `006dafd0` | `15 58 42 a9` | ldp x21,x22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-006dafd4"></a> `006dafd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006dafd8"></a> `006dafd8` | `14 00 40 b9` | ldr w20,[x0] | `FALL_THROUGH`
<a id="insn-006dafdc"></a> `006dafdc` | `88 02 01 0b` | add w8,w20,w1 | `FALL_THROUGH`
<a id="insn-006dafe0"></a> `006dafe0` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006dafe4"></a> `006dafe4` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-006dafe8"></a> `006dafe8` | `c1 00 00 54` | b.ne 0x006db000 | `CONDITIONAL_JUMP`
<a id="insn-006dafec"></a> `006dafec` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-006daff0"></a> `006daff0` | `17 00 00 14` | b 0x006db04c | `UNCONDITIONAL_JUMP`
<a id="insn-006daff4"></a> `006daff4` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006daff8"></a> `006daff8` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006daffc"></a> `006daffc` | `80 ff ff 54` | b.eq 0x006dafec | `CONDITIONAL_JUMP`
<a id="insn-006db000"></a> `006db000` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-006db004"></a> `006db004` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-006db008"></a> `006db008` | `6d ff ff 54` | b.le 0x006daff4 | `CONDITIONAL_JUMP`
<a id="insn-006db00c"></a> `006db00c` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-006db010"></a> `006db010` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-006db014"></a> `006db014` | `0c ff ff 54` | b.gt 0x006daff4 | `CONDITIONAL_JUMP`
<a id="insn-006db018"></a> `006db018` | `b7 06 40 b9` | ldr w23,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-006db01c"></a> `006db01c` | `00 7d 80 52` | mov w0,#0x3e8 | `FALL_THROUGH`
<a id="insn-006db020"></a> `006db020` | `f4 49 f6 97` | bl 0x0046d7f0 | `UNCONDITIONAL_CALL`
<a id="insn-006db024"></a> `006db024` | `ff 02 00 6b` | cmp w23,w0 | `FALL_THROUGH`
<a id="insn-006db028"></a> `006db028` | `6d fe ff 54` | b.le 0x006daff4 | `CONDITIONAL_JUMP`
<a id="insn-006db02c"></a> `006db02c` | `68 26 43 29` | ldp w8,w9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-006db030"></a> `006db030` | `7f 02 00 b9` | str wzr,[x19] | `FALL_THROUGH`
<a id="insn-006db034"></a> `006db034` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-006db038"></a> `006db038` | `0a 65 1a 53` | lsl w10,w8,#0x6 | `FALL_THROUGH`
<a id="insn-006db03c"></a> `006db03c` | `69 12 00 b9` | str w9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006db040"></a> `006db040` | `48 09 08 4b` | sub w8,w10,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006db044"></a> `006db044` | `00 01 62 1e` | scvtf d0,w8 | `FALL_THROUGH`
<a id="insn-006db048"></a> `006db048` | `60 06 00 fd` | str d0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006db04c"></a> `006db04c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006db050"></a> `006db050` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006db054"></a> `006db054` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006db058"></a> `006db058` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-006db05c"></a> `006db05c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dafac`](#insn-006dafac) 範囲 `[['006dafac', '006dafb3']]`
  - `CONDITIONAL_JUMP` [`006dafb0`](#insn-006dafb0) → [`006dafbc`](#insn-006dafbc)
  - `FALL_THROUGH` [`006dafb0`](#insn-006dafb0) → [`006dafb4`](#insn-006dafb4)
- ブロック [`006dafb4`](#insn-006dafb4) 範囲 `[['006dafb4', '006dafbb']]`
- ブロック [`006dafbc`](#insn-006dafbc) 範囲 `[['006dafbc', '006dafeb']]`
  - `CONDITIONAL_JUMP` [`006dafe8`](#insn-006dafe8) → [`006db000`](#insn-006db000)
  - `FALL_THROUGH` [`006dafe8`](#insn-006dafe8) → [`006dafec`](#insn-006dafec)
- ブロック [`006dafec`](#insn-006dafec) 範囲 `[['006dafec', '006daff3']]`
  - `UNCONDITIONAL_JUMP` [`006daff0`](#insn-006daff0) → [`006db04c`](#insn-006db04c)
- ブロック [`006daff4`](#insn-006daff4) 範囲 `[['006daff4', '006dafff']]`
  - `CONDITIONAL_JUMP` [`006daffc`](#insn-006daffc) → [`006dafec`](#insn-006dafec)
  - `FALL_THROUGH` [`006daffc`](#insn-006daffc) → [`006db000`](#insn-006db000)
- ブロック [`006db000`](#insn-006db000) 範囲 `[['006db000', '006db00b']]`
  - `CONDITIONAL_JUMP` [`006db008`](#insn-006db008) → [`006daff4`](#insn-006daff4)
  - `FALL_THROUGH` [`006db008`](#insn-006db008) → [`006db00c`](#insn-006db00c)
- ブロック [`006db00c`](#insn-006db00c) 範囲 `[['006db00c', '006db017']]`
  - `CONDITIONAL_JUMP` [`006db014`](#insn-006db014) → [`006daff4`](#insn-006daff4)
  - `FALL_THROUGH` [`006db014`](#insn-006db014) → [`006db018`](#insn-006db018)
- ブロック [`006db018`](#insn-006db018) 範囲 `[['006db018', '006db02b']]`
  - `CONDITIONAL_JUMP` [`006db028`](#insn-006db028) → [`006daff4`](#insn-006daff4)
  - `FALL_THROUGH` [`006db028`](#insn-006db028) → [`006db02c`](#insn-006db02c)
- ブロック [`006db02c`](#insn-006db02c) 範囲 `[['006db02c', '006db04b']]`
  - `FALL_THROUGH` [`006db048`](#insn-006db048) → [`006db04c`](#insn-006db04c)
- ブロック [`006db04c`](#insn-006db04c) 範囲 `[['006db04c', '006db05f']]`

## 命令位置別の参照

- [`006dafb0`](#insn-006dafb0) → [`006dafbc`](#insn-006dafbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafbc`](#insn-006dafbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafc0`](#insn-006dafc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafc4`](#insn-006dafc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafc8`](#insn-006dafc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dafe8`](#insn-006dafe8) → [`006db000`](#insn-006db000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daff0`](#insn-006daff0) → [`006db04c`](#insn-006db04c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daffc`](#insn-006daffc) → [`006dafec`](#insn-006dafec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db008`](#insn-006db008) → [`006daff4`](#insn-006daff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db014`](#insn-006db014) → [`006daff4`](#insn-006daff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db020`](#insn-006db020) → [`0046d7f0`](../0046d/0046d7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d7f0` · 推定シンボル `None` · 推定型 `None`
- [`006db028`](#insn-006db028) → [`006daff4`](#insn-006daff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db04c`](#insn-006db04c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db050`](#insn-006db050) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db054`](#insn-006db054) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006db058`](#insn-006db058) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dafb0`](#insn-006dafb0)

~~~json
{
  "source": "006dafb0",
  "target": "006dafbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafbc`](#insn-006dafbc)

~~~json
{
  "source": "006dafbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafc0`](#insn-006dafc0)

~~~json
{
  "source": "006dafc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafc4`](#insn-006dafc4)

~~~json
{
  "source": "006dafc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafc8`](#insn-006dafc8)

~~~json
{
  "source": "006dafc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dafe8`](#insn-006dafe8)

~~~json
{
  "source": "006dafe8",
  "target": "006db000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daff0`](#insn-006daff0)

~~~json
{
  "source": "006daff0",
  "target": "006db04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daffc`](#insn-006daffc)

~~~json
{
  "source": "006daffc",
  "target": "006dafec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db008`](#insn-006db008)

~~~json
{
  "source": "006db008",
  "target": "006daff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db014`](#insn-006db014)

~~~json
{
  "source": "006db014",
  "target": "006daff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db020`](#insn-006db020)

~~~json
{
  "source": "006db020",
  "target": "0046d7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006db028`](#insn-006db028)

~~~json
{
  "source": "006db028",
  "target": "006daff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db04c`](#insn-006db04c)

~~~json
{
  "source": "006db04c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db050`](#insn-006db050)

~~~json
{
  "source": "006db050",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db054`](#insn-006db054)

~~~json
{
  "source": "006db054",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006db058`](#insn-006db058)

~~~json
{
  "source": "006db058",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
