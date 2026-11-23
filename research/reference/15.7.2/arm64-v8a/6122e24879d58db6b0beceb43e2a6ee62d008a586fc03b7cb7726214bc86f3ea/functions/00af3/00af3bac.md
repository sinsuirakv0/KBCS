# 00af3bac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af3c74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3c74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0008.md#compare-4a35ac895adb245fc1b3b412c068bd1e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3bac",
  "name": "_ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "087819567e945be810abefedcbcc6b15dd026294c2200781bf45aa233933984a",
  "source_text_sha256": "087819567e945be810abefedcbcc6b15dd026294c2200781bf45aa233933984a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3bac",
        "00af3c4f"
      ]
    ],
    "bytes_sha256": "b2357c4bd59bf08b4cf2476a687dcd88ecc85b3ae7f2df2b44969e44eb6efd06",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bddfa0](../00bdd/00bddfa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 706 bytes

~~~c

void _ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject(undefined8 param_1,long *param_2)

{
  char cVar1;
  undefined8 uVar2;
  
  uVar2 = (**(code **)(*param_2 + 0xf8))();
  uVar2 = FUN_0047495c(param_2,uVar2,DAT_010a05b0);
  cVar1 = (**(code **)(*param_2 + 0x720))(param_2);
  if (cVar1 != '\0') {
    (**(code **)(*param_2 + 0x80))(param_2);
    (**(code **)(*param_2 + 0x88))(param_2);
  }
  _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(param_1,param_2,uVar2);
                    /* WARNING: Could not recover jumptable at 0x00af3c4c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_2 + 0xb8))(param_2,uVar2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3bac"></a> `00af3bac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af3bb0"></a> `00af3bb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3bb4"></a> `00af3bb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af3bb8"></a> `00af3bb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00af3bbc"></a> `00af3bbc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00af3bc0"></a> `00af3bc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af3bc4"></a> `00af3bc4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00af3bc8"></a> `00af3bc8` | `29 7d 40 f9` | ldr x9,[x9, #0xf8] | `FALL_THROUGH`
<a id="insn-00af3bcc"></a> `00af3bcc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00af3bd0"></a> `00af3bd0` | `68 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af3bd4"></a> `00af3bd4` | `02 d9 42 f9` | ldr x2,[x8, #0x5b0] | `FALL_THROUGH`
<a id="insn-00af3bd8"></a> `00af3bd8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00af3bdc"></a> `00af3bdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3be0"></a> `00af3be0` | `5f 03 e6 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00af3be4"></a> `00af3be4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3be8"></a> `00af3be8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af3bec"></a> `00af3bec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3bf0"></a> `00af3bf0` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af3bf4"></a> `00af3bf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3bf8"></a> `00af3bf8` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af3bfc"></a> `00af3bfc` | `20 01 00 54` | b.eq 0x00af3c20 | `CONDITIONAL_JUMP`
<a id="insn-00af3c00"></a> `00af3c00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3c04"></a> `00af3c04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3c08"></a> `00af3c08` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af3c0c"></a> `00af3c0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3c10"></a> `00af3c10` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3c14"></a> `00af3c14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3c18"></a> `00af3c18` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af3c1c"></a> `00af3c1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3c20"></a> `00af3c20` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00af3c24"></a> `00af3c24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3c28"></a> `00af3c28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af3c2c"></a> `00af3c2c` | `dd a8 03 94` | bl 0x00bddfa0 | `UNCONDITIONAL_CALL`
<a id="insn-00af3c30"></a> `00af3c30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3c34"></a> `00af3c34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3c38"></a> `00af3c38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af3c3c"></a> `00af3c3c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3c40"></a> `00af3c40` | `02 5d 40 f9` | ldr x2,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af3c44"></a> `00af3c44` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af3c48"></a> `00af3c48` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af3c4c"></a> `00af3c4c` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af3bac`](#insn-00af3bac) 範囲 `[['00af3bac', '00af3bff']]`
  - `CONDITIONAL_JUMP` [`00af3bfc`](#insn-00af3bfc) → [`00af3c20`](#insn-00af3c20)
  - `FALL_THROUGH` [`00af3bfc`](#insn-00af3bfc) → [`00af3c00`](#insn-00af3c00)
- ブロック [`00af3c00`](#insn-00af3c00) 範囲 `[['00af3c00', '00af3c1f']]`
  - `FALL_THROUGH` [`00af3c1c`](#insn-00af3c1c) → [`00af3c20`](#insn-00af3c20)
- ブロック [`00af3c20`](#insn-00af3c20) 範囲 `[['00af3c20', '00af3c4f']]`

## 命令位置別の参照

- [`00af3bac`](#insn-00af3bac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3bb0`](#insn-00af3bb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3bb4`](#insn-00af3bb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3bd4`](#insn-00af3bd4) → `010a05b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af3be0`](#insn-00af3be0) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00af3bfc`](#insn-00af3bfc) → [`00af3c20`](#insn-00af3c20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3c2c`](#insn-00af3c2c) → [`00bddfa0`](../00bdd/00bddfa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfa0` · 推定シンボル `None` · 推定型 `None`
- [`00af3c38`](#insn-00af3c38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3c3c`](#insn-00af3c3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3bac`](#insn-00af3bac)

~~~json
{
  "source": "00af3bac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3bb0`](#insn-00af3bb0)

~~~json
{
  "source": "00af3bb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3bb4`](#insn-00af3bb4)

~~~json
{
  "source": "00af3bb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3bd4`](#insn-00af3bd4)

~~~json
{
  "source": "00af3bd4",
  "target": "010a05b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a05b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af3be0`](#insn-00af3be0)

~~~json
{
  "source": "00af3be0",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3bfc`](#insn-00af3bfc)

~~~json
{
  "source": "00af3bfc",
  "target": "00af3c20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3c2c`](#insn-00af3c2c)

~~~json
{
  "source": "00af3c2c",
  "target": "00bddfa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3c38`](#insn-00af3c38)

~~~json
{
  "source": "00af3c38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3c3c`](#insn-00af3c3c)

~~~json
{
  "source": "00af3c3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
