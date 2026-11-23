# 00acbcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acbc08`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-97f074ca5982662c546c823a8415ff7f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acbd14`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-2d122cdcfaad15f1e6eb8bac785d5148)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbcd0",
  "name": "FUN_00acbcd0",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77",
  "source_text_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbcd0",
        "00acbd33"
      ]
    ],
    "bytes_sha256": "37af7ead967ea36844394137d95c34cd8042a78c139811e3b82bb9e52fc98ef5",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00418a68](../00418/00418a68.md)
- [00418b18](../00418/00418b18.md)

## 呼び出し先

- [00449bcc](../00449/00449bcc.md)
- [00449be4](../00449/00449be4.md)
- [00449bf0](../00449/00449bf0.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00acbcd0(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_0081f580();
  if ((param_2 & 1) == 0) {
    FUN_00449bcc(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_00449be4();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_0081f580();
      FUN_00449bf0(uVar2,0);
    }
    uVar2 = FUN_0081f580();
    FUN_00449bcc(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acbd30. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbcd0"></a> `00acbcd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acbcd4"></a> `00acbcd4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbcd8"></a> `00acbcd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbcdc"></a> `00acbcdc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acbce0"></a> `00acbce0` | `28 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbce4"></a> `00acbce4` | `73 01 00 36` | tbz w19,#0x0,0x00acbd10 | `CONDITIONAL_JUMP`
<a id="insn-00acbce8"></a> `00acbce8` | `bf f7 e5 97` | bl 0x00449be4 | `UNCONDITIONAL_CALL`
<a id="insn-00acbcec"></a> `00acbcec` | `80 00 00 36` | tbz w0,#0x0,0x00acbcfc | `CONDITIONAL_JUMP`
<a id="insn-00acbcf0"></a> `00acbcf0` | `24 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbcf4"></a> `00acbcf4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acbcf8"></a> `00acbcf8` | `be f7 e5 97` | bl 0x00449bf0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbcfc"></a> `00acbcfc` | `21 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd00"></a> `00acbd00` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acbd04"></a> `00acbd04` | `b2 f7 e5 97` | bl 0x00449bcc | `UNCONDITIONAL_CALL`
<a id="insn-00acbd08"></a> `00acbd08` | `13 02 80 52` | mov w19,#0x10 | `FALL_THROUGH`
<a id="insn-00acbd0c"></a> `00acbd0c` | `04 00 00 14` | b 0x00acbd1c | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd10"></a> `00acbd10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acbd14"></a> `00acbd14` | `ae f7 e5 97` | bl 0x00449bcc | `UNCONDITIONAL_CALL`
<a id="insn-00acbd18"></a> `00acbd18` | `13 03 80 52` | mov w19,#0x18 | `FALL_THROUGH`
<a id="insn-00acbd1c"></a> `00acbd1c` | `19 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd20"></a> `00acbd20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbd24"></a> `00acbd24` | `01 69 73 f8` | ldr x1,[x8, x19, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acbd28"></a> `00acbd28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbd2c"></a> `00acbd2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acbd30"></a> `00acbd30` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00acbcd0`](#insn-00acbcd0) 範囲 `[['00acbcd0', '00acbce7']]`
  - `CONDITIONAL_JUMP` [`00acbce4`](#insn-00acbce4) → [`00acbd10`](#insn-00acbd10)
  - `FALL_THROUGH` [`00acbce4`](#insn-00acbce4) → [`00acbce8`](#insn-00acbce8)
- ブロック [`00acbce8`](#insn-00acbce8) 範囲 `[['00acbce8', '00acbcef']]`
  - `CONDITIONAL_JUMP` [`00acbcec`](#insn-00acbcec) → [`00acbcfc`](#insn-00acbcfc)
  - `FALL_THROUGH` [`00acbcec`](#insn-00acbcec) → [`00acbcf0`](#insn-00acbcf0)
- ブロック [`00acbcf0`](#insn-00acbcf0) 範囲 `[['00acbcf0', '00acbcfb']]`
  - `FALL_THROUGH` [`00acbcf8`](#insn-00acbcf8) → [`00acbcfc`](#insn-00acbcfc)
- ブロック [`00acbcfc`](#insn-00acbcfc) 範囲 `[['00acbcfc', '00acbd0f']]`
  - `UNCONDITIONAL_JUMP` [`00acbd0c`](#insn-00acbd0c) → [`00acbd1c`](#insn-00acbd1c)
- ブロック [`00acbd10`](#insn-00acbd10) 範囲 `[['00acbd10', '00acbd1b']]`
  - `FALL_THROUGH` [`00acbd18`](#insn-00acbd18) → [`00acbd1c`](#insn-00acbd1c)
- ブロック [`00acbd1c`](#insn-00acbd1c) 範囲 `[['00acbd1c', '00acbd33']]`

## 命令位置別の参照

- [`00acbcd0`](#insn-00acbcd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcd4`](#insn-00acbcd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbce0`](#insn-00acbce0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbce4`](#insn-00acbce4) → [`00acbd10`](#insn-00acbd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbce8`](#insn-00acbce8) → [`00449be4`](../00449/00449be4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449be4` · 推定シンボル `None` · 推定型 `None`
- [`00acbcec`](#insn-00acbcec) → [`00acbcfc`](#insn-00acbcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcf0`](#insn-00acbcf0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbcf8`](#insn-00acbcf8) → [`00449bf0`](../00449/00449bf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bf0` · 推定シンボル `None` · 推定型 `None`
- [`00acbcfc`](#insn-00acbcfc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbd04`](#insn-00acbd04) → [`00449bcc`](../00449/00449bcc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bcc` · 推定シンボル `None` · 推定型 `None`
- [`00acbd0c`](#insn-00acbd0c) → [`00acbd1c`](#insn-00acbd1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd14`](#insn-00acbd14) → [`00449bcc`](../00449/00449bcc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bcc` · 推定シンボル `None` · 推定型 `None`
- [`00acbd1c`](#insn-00acbd1c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbd28`](#insn-00acbd28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd2c`](#insn-00acbd2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbcd0`](#insn-00acbcd0)

~~~json
{
  "source": "00acbcd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcd4`](#insn-00acbcd4)

~~~json
{
  "source": "00acbcd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbce0`](#insn-00acbce0)

~~~json
{
  "source": "00acbce0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbce4`](#insn-00acbce4)

~~~json
{
  "source": "00acbce4",
  "target": "00acbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbce8`](#insn-00acbce8)

~~~json
{
  "source": "00acbce8",
  "target": "00449be4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbcec`](#insn-00acbcec)

~~~json
{
  "source": "00acbcec",
  "target": "00acbcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcf0`](#insn-00acbcf0)

~~~json
{
  "source": "00acbcf0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbcf8`](#insn-00acbcf8)

~~~json
{
  "source": "00acbcf8",
  "target": "00449bf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbcfc`](#insn-00acbcfc)

~~~json
{
  "source": "00acbcfc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd04`](#insn-00acbd04)

~~~json
{
  "source": "00acbd04",
  "target": "00449bcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd0c`](#insn-00acbd0c)

~~~json
{
  "source": "00acbd0c",
  "target": "00acbd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd14`](#insn-00acbd14)

~~~json
{
  "source": "00acbd14",
  "target": "00449bcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd1c`](#insn-00acbd1c)

~~~json
{
  "source": "00acbd1c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd28`](#insn-00acbd28)

~~~json
{
  "source": "00acbd28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd2c`](#insn-00acbd2c)

~~~json
{
  "source": "00acbd2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
