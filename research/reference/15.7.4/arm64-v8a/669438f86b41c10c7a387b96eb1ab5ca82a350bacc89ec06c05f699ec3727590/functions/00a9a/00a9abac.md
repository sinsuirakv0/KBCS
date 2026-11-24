# 00a9abac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9ab68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9ab68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0005.md#compare-3180bfdd34a31f3dc6fdbd2ca4f4fc9d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0086.md#review-c57998241747bec18de3525678af8e22)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9abac",
  "name": "FUN_00a9abac",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "388155e63b9b3529b9a511d54594e795eb806d86bd5ada6e64ed731ac76502d8",
  "source_text_sha256": "388155e63b9b3529b9a511d54594e795eb806d86bd5ada6e64ed731ac76502d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9abac",
        "00a9ac13"
      ]
    ],
    "bytes_sha256": "ab0d5fb3150978acf78b4f1b107792b7ae95fd87e72e70f73c583633ec3bb434",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006e79bc](../006e7/006e79bc.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

undefined4 FUN_00a9abac(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_0081f580();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x843c0);
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9abac"></a> `00a9abac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a9abb0"></a> `00a9abb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9abb4"></a> `00a9abb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9abb8"></a> `00a9abb8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00a9abbc"></a> `00a9abbc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9abc0"></a> `00a9abc0` | `70 12 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9abc4"></a> `00a9abc4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00a9abc8"></a> `00a9abc8` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00a9abcc"></a> `00a9abcc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9abd0"></a> `00a9abd0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00a9abd4"></a> `00a9abd4` | `cf 9e ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9abd8"></a> `00a9abd8` | `60 00 00 37` | tbnz w0,#0x0,0x00a9abe4 | `CONDITIONAL_JUMP`
<a id="insn-00a9abdc"></a> `00a9abdc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9abe0"></a> `00a9abe0` | `0a 00 00 14` | b 0x00a9ac08 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9abe4"></a> `00a9abe4` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00a9abe8"></a> `00a9abe8` | `66 12 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9abec"></a> `00a9abec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9abf0"></a> `00a9abf0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9abf4"></a> `00a9abf4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9abf8"></a> `00a9abf8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9abfc"></a> `00a9abfc` | `09 78 88 52` | mov w9,#0x43c0 | `FALL_THROUGH`
<a id="insn-00a9ac00"></a> `00a9ac00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ac04"></a> `00a9ac04` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ac08"></a> `00a9ac08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ac0c"></a> `00a9ac0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a9ac10"></a> `00a9ac10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9abac`](#insn-00a9abac) 範囲 `[['00a9abac', '00a9abdb']]`
  - `CONDITIONAL_JUMP` [`00a9abd8`](#insn-00a9abd8) → [`00a9abe4`](#insn-00a9abe4)
  - `FALL_THROUGH` [`00a9abd8`](#insn-00a9abd8) → [`00a9abdc`](#insn-00a9abdc)
- ブロック [`00a9abdc`](#insn-00a9abdc) 範囲 `[['00a9abdc', '00a9abe3']]`
  - `UNCONDITIONAL_JUMP` [`00a9abe0`](#insn-00a9abe0) → [`00a9ac08`](#insn-00a9ac08)
- ブロック [`00a9abe4`](#insn-00a9abe4) 範囲 `[['00a9abe4', '00a9ac07']]`
  - `FALL_THROUGH` [`00a9ac04`](#insn-00a9ac04) → [`00a9ac08`](#insn-00a9ac08)
- ブロック [`00a9ac08`](#insn-00a9ac08) 範囲 `[['00a9ac08', '00a9ac13']]`

## 命令位置別の参照

- [`00a9abac`](#insn-00a9abac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abb0`](#insn-00a9abb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abc0`](#insn-00a9abc0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9abd4`](#insn-00a9abd4) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9abd8`](#insn-00a9abd8) → [`00a9abe4`](#insn-00a9abe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abe0`](#insn-00a9abe0) → [`00a9ac08`](#insn-00a9ac08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abe8`](#insn-00a9abe8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac08`](#insn-00a9ac08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac0c`](#insn-00a9ac0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9abac`](#insn-00a9abac)

~~~json
{
  "source": "00a9abac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abb0`](#insn-00a9abb0)

~~~json
{
  "source": "00a9abb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abc0`](#insn-00a9abc0)

~~~json
{
  "source": "00a9abc0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9abd4`](#insn-00a9abd4)

~~~json
{
  "source": "00a9abd4",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9abd8`](#insn-00a9abd8)

~~~json
{
  "source": "00a9abd8",
  "target": "00a9abe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abe0`](#insn-00a9abe0)

~~~json
{
  "source": "00a9abe0",
  "target": "00a9ac08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abe8`](#insn-00a9abe8)

~~~json
{
  "source": "00a9abe8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac08`](#insn-00a9ac08)

~~~json
{
  "source": "00a9ac08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac0c`](#insn-00a9ac0c)

~~~json
{
  "source": "00a9ac0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
