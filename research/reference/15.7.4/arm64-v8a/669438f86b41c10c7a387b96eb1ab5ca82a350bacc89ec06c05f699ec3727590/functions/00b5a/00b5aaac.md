# 00b5aaac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5aa68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0012.md#compare-a7120a3431571ef3302bae0d09bc8a33)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc9fac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9fac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-a27e0893772688337380b0ea426b2297)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5aaac",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51bada066e8c19e9ff377a53625919d7f937b3306eeaad2de633beb3a567c73e",
  "source_text_sha256": "51bada066e8c19e9ff377a53625919d7f937b3306eeaad2de633beb3a567c73e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5aaac",
        "00b5ab23"
      ]
    ],
    "bytes_sha256": "1c511cbb5f1ba776960db6434f125717344959f4aa409bac0b98991578d8c0f8",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00be06b0](../00be0/00be06b0.md)

## 呼び出し先

- [00b010ec](../00b01/00b010ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1027 bytes

~~~c

void _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev
               (long param_1)

{
  long *plVar1;
  code *UNRECOVERED_JUMPTABLE;
  
  if (*(char *)(param_1 + 0x40) == '\0') {
    *(undefined1 *)(param_1 + 0x40) = 1;
    if (*(long **)(param_1 + 0x30) == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b010ec();
    }
    (**(code **)(**(long **)(param_1 + 0x30) + 0x30))();
  }
                    /* try { // try from 00b5aae0 to 00c5ac0b has its CatchHandler @ 00b5af44 */
  plVar1 = *(long **)(param_1 + 0x30);
  if ((long *)(param_1 + 0x10) == plVar1) {
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x20);
  }
  else {
    if (plVar1 == (long *)0x0) {
      return;
    }
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x28);
  }
                    /* WARNING: Could not recover jumptable at 0x00b5ab10. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*UNRECOVERED_JUMPTABLE)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5aaac"></a> `00b5aaac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b5aab0"></a> `00b5aab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5aab4"></a> `00b5aab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b5aab8"></a> `00b5aab8` | `08 00 41 39` | ldrb w8,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00b5aabc"></a> `00b5aabc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5aac0"></a> `00b5aac0` | `08 01 00 35` | cbnz w8,0x00b5aae0 | `CONDITIONAL_JUMP`
<a id="insn-00b5aac4"></a> `00b5aac4` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b5aac8"></a> `00b5aac8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5aacc"></a> `00b5aacc` | `68 02 01 39` | strb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b5aad0"></a> `00b5aad0` | `80 02 00 b4` | cbz x0,0x00b5ab20 | `CONDITIONAL_JUMP`
<a id="insn-00b5aad4"></a> `00b5aad4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5aad8"></a> `00b5aad8` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00b5aadc"></a> `00b5aadc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5aae0"></a> `00b5aae0` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b5aae4"></a> `00b5aae4` | `68 42 00 91` | add x8,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00b5aae8"></a> `00b5aae8` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00b5aaec"></a> `00b5aaec` | `a0 00 00 54` | b.eq 0x00b5ab00 | `CONDITIONAL_JUMP`
<a id="insn-00b5aaf0"></a> `00b5aaf0` | `20 01 00 b4` | cbz x0,0x00b5ab14 | `CONDITIONAL_JUMP`
<a id="insn-00b5aaf4"></a> `00b5aaf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5aaf8"></a> `00b5aaf8` | `01 15 40 f9` | ldr x1,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b5aafc"></a> `00b5aafc` | `03 00 00 14` | b 0x00b5ab08 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ab00"></a> `00b5ab00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5ab04"></a> `00b5ab04` | `01 11 40 f9` | ldr x1,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ab08"></a> `00b5ab08` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ab0c"></a> `00b5ab0c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5ab10"></a> `00b5ab10` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00b5ab14"></a> `00b5ab14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ab18"></a> `00b5ab18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5ab1c"></a> `00b5ab1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5ab20"></a> `00b5ab20` | `73 99 fe 97` | bl 0x00b010ec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5aaac`](#insn-00b5aaac) 範囲 `[['00b5aaac', '00b5aac3']]`
  - `CONDITIONAL_JUMP` [`00b5aac0`](#insn-00b5aac0) → [`00b5aae0`](#insn-00b5aae0)
  - `FALL_THROUGH` [`00b5aac0`](#insn-00b5aac0) → [`00b5aac4`](#insn-00b5aac4)
- ブロック [`00b5aac4`](#insn-00b5aac4) 範囲 `[['00b5aac4', '00b5aad3']]`
  - `CONDITIONAL_JUMP` [`00b5aad0`](#insn-00b5aad0) → [`00b5ab20`](#insn-00b5ab20)
  - `FALL_THROUGH` [`00b5aad0`](#insn-00b5aad0) → [`00b5aad4`](#insn-00b5aad4)
- ブロック [`00b5aad4`](#insn-00b5aad4) 範囲 `[['00b5aad4', '00b5aadf']]`
  - `FALL_THROUGH` [`00b5aadc`](#insn-00b5aadc) → [`00b5aae0`](#insn-00b5aae0)
- ブロック [`00b5aae0`](#insn-00b5aae0) 範囲 `[['00b5aae0', '00b5aaef']]`
  - `CONDITIONAL_JUMP` [`00b5aaec`](#insn-00b5aaec) → [`00b5ab00`](#insn-00b5ab00)
  - `FALL_THROUGH` [`00b5aaec`](#insn-00b5aaec) → [`00b5aaf0`](#insn-00b5aaf0)
- ブロック [`00b5aaf0`](#insn-00b5aaf0) 範囲 `[['00b5aaf0', '00b5aaf3']]`
  - `CONDITIONAL_JUMP` [`00b5aaf0`](#insn-00b5aaf0) → [`00b5ab14`](#insn-00b5ab14)
  - `FALL_THROUGH` [`00b5aaf0`](#insn-00b5aaf0) → [`00b5aaf4`](#insn-00b5aaf4)
- ブロック [`00b5aaf4`](#insn-00b5aaf4) 範囲 `[['00b5aaf4', '00b5aaff']]`
  - `UNCONDITIONAL_JUMP` [`00b5aafc`](#insn-00b5aafc) → [`00b5ab08`](#insn-00b5ab08)
- ブロック [`00b5ab00`](#insn-00b5ab00) 範囲 `[['00b5ab00', '00b5ab07']]`
  - `FALL_THROUGH` [`00b5ab04`](#insn-00b5ab04) → [`00b5ab08`](#insn-00b5ab08)
- ブロック [`00b5ab08`](#insn-00b5ab08) 範囲 `[['00b5ab08', '00b5ab13']]`
- ブロック [`00b5ab14`](#insn-00b5ab14) 範囲 `[['00b5ab14', '00b5ab1f']]`
- ブロック [`00b5ab20`](#insn-00b5ab20) 範囲 `[['00b5ab20', '00b5ab23']]`

## 命令位置別の参照

- [`00b5aaac`](#insn-00b5aaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aab0`](#insn-00b5aab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aac0`](#insn-00b5aac0) → [`00b5aae0`](#insn-00b5aae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aad0`](#insn-00b5aad0) → [`00b5ab20`](#insn-00b5ab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aaec`](#insn-00b5aaec) → [`00b5ab00`](#insn-00b5ab00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aaf0`](#insn-00b5aaf0) → [`00b5ab14`](#insn-00b5ab14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aafc`](#insn-00b5aafc) → [`00b5ab08`](#insn-00b5ab08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ab08`](#insn-00b5ab08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ab14`](#insn-00b5ab14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ab20`](#insn-00b5ab20) → [`00b010ec`](../00b01/00b010ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b010ec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5aaac`](#insn-00b5aaac)

~~~json
{
  "source": "00b5aaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aab0`](#insn-00b5aab0)

~~~json
{
  "source": "00b5aab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aac0`](#insn-00b5aac0)

~~~json
{
  "source": "00b5aac0",
  "target": "00b5aae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aad0`](#insn-00b5aad0)

~~~json
{
  "source": "00b5aad0",
  "target": "00b5ab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aaec`](#insn-00b5aaec)

~~~json
{
  "source": "00b5aaec",
  "target": "00b5ab00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aaf0`](#insn-00b5aaf0)

~~~json
{
  "source": "00b5aaf0",
  "target": "00b5ab14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aafc`](#insn-00b5aafc)

~~~json
{
  "source": "00b5aafc",
  "target": "00b5ab08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ab08`](#insn-00b5ab08)

~~~json
{
  "source": "00b5ab08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ab14`](#insn-00b5ab14)

~~~json
{
  "source": "00b5ab14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ab20`](#insn-00b5ab20)

~~~json
{
  "source": "00b5ab20",
  "target": "00b010ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
