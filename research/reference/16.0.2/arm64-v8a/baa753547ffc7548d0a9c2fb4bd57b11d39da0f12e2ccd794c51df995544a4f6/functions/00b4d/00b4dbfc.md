# 00b4dbfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4db60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0074.md#compare-d9a3600d7401079c5acc1e340775694f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4ebf0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4ebf0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0076.md#compare-bd335e0f8469a67a512ee10fef881cf3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dbfc",
  "name": "_ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd1c26f13a137cf35f6cc4f554757dc258c11bd53d07aa42d589d32e2129dd00",
  "source_text_sha256": "cd1c26f13a137cf35f6cc4f554757dc258c11bd53d07aa42d589d32e2129dd00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dbfc",
        "00b4dc97"
      ]
    ],
    "bytes_sha256": "5afb1824993154c89d9cddb2127ab5830310706a86f26bd1505e69a9a955f4b1",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 607 bytes

~~~c

bool _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_01125df8 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01125df0,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_01125df8 = iVar3 == 0;
    bVar2 = (bool)DAT_01125df8;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4dbfc"></a> `00b4dbfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4dc00"></a> `00b4dc00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dc04"></a> `00b4dc04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4dc08"></a> `00b4dc08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4dc0c"></a> `00b4dc0c` | `d5 2e 00 90` | adrp x21,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4dc10"></a> `00b4dc10` | `a8 e2 77 39` | ldrb w8,[x21, #0xdf8] | `FALL_THROUGH`
<a id="insn-00b4dc14"></a> `00b4dc14` | `68 00 00 34` | cbz w8,0x00b4dc20 | `CONDITIONAL_JUMP`
<a id="insn-00b4dc18"></a> `00b4dc18` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b4dc1c"></a> `00b4dc1c` | `1b 00 00 14` | b 0x00b4dc88 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4dc20"></a> `00b4dc20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b4dc24"></a> `00b4dc24` | `c9 2e 00 90` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4dc28"></a> `00b4dc28` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00b4dc2c"></a> `00b4dc2c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00b4dc30"></a> `00b4dc30` | `21 f9 46 f9` | ldr x1,[x9, #0xdf0] | `FALL_THROUGH`
<a id="insn-00b4dc34"></a> `00b4dc34` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00b4dc38"></a> `00b4dc38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4dc3c"></a> `00b4dc3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc40"></a> `00b4dc40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4dc44"></a> `00b4dc44` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b4dc48"></a> `00b4dc48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc4c"></a> `00b4dc4c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4dc50"></a> `00b4dc50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc54"></a> `00b4dc54` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4dc58"></a> `00b4dc58` | `20 01 00 54` | b.eq 0x00b4dc7c | `CONDITIONAL_JUMP`
<a id="insn-00b4dc5c"></a> `00b4dc5c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4dc60"></a> `00b4dc60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc64"></a> `00b4dc64` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4dc68"></a> `00b4dc68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc6c"></a> `00b4dc6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4dc70"></a> `00b4dc70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc74"></a> `00b4dc74` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4dc78"></a> `00b4dc78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc7c"></a> `00b4dc7c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00b4dc80"></a> `00b4dc80` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00b4dc84"></a> `00b4dc84` | `a0 e2 37 39` | strb w0,[x21, #0xdf8] | `FALL_THROUGH`
<a id="insn-00b4dc88"></a> `00b4dc88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4dc8c"></a> `00b4dc8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dc90"></a> `00b4dc90` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4dc94"></a> `00b4dc94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dbfc`](#insn-00b4dbfc) 範囲 `[['00b4dbfc', '00b4dc17']]`
  - `CONDITIONAL_JUMP` [`00b4dc14`](#insn-00b4dc14) → [`00b4dc20`](#insn-00b4dc20)
  - `FALL_THROUGH` [`00b4dc14`](#insn-00b4dc14) → [`00b4dc18`](#insn-00b4dc18)
- ブロック [`00b4dc18`](#insn-00b4dc18) 範囲 `[['00b4dc18', '00b4dc1f']]`
  - `UNCONDITIONAL_JUMP` [`00b4dc1c`](#insn-00b4dc1c) → [`00b4dc88`](#insn-00b4dc88)
- ブロック [`00b4dc20`](#insn-00b4dc20) 範囲 `[['00b4dc20', '00b4dc5b']]`
  - `CONDITIONAL_JUMP` [`00b4dc58`](#insn-00b4dc58) → [`00b4dc7c`](#insn-00b4dc7c)
  - `FALL_THROUGH` [`00b4dc58`](#insn-00b4dc58) → [`00b4dc5c`](#insn-00b4dc5c)
- ブロック [`00b4dc5c`](#insn-00b4dc5c) 範囲 `[['00b4dc5c', '00b4dc7b']]`
  - `FALL_THROUGH` [`00b4dc78`](#insn-00b4dc78) → [`00b4dc7c`](#insn-00b4dc7c)
- ブロック [`00b4dc7c`](#insn-00b4dc7c) 範囲 `[['00b4dc7c', '00b4dc87']]`
  - `FALL_THROUGH` [`00b4dc84`](#insn-00b4dc84) → [`00b4dc88`](#insn-00b4dc88)
- ブロック [`00b4dc88`](#insn-00b4dc88) 範囲 `[['00b4dc88', '00b4dc97']]`

## 命令位置別の参照

- [`00b4dbfc`](#insn-00b4dbfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc00`](#insn-00b4dc00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc04`](#insn-00b4dc04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc10`](#insn-00b4dc10) → `01125df8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4dc14`](#insn-00b4dc14) → [`00b4dc20`](#insn-00b4dc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc1c`](#insn-00b4dc1c) → [`00b4dc88`](#insn-00b4dc88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc30`](#insn-00b4dc30) → `01125df0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dc58`](#insn-00b4dc58) → [`00b4dc7c`](#insn-00b4dc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc84`](#insn-00b4dc84) → `01125df8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4dc88`](#insn-00b4dc88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc8c`](#insn-00b4dc8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dbfc`](#insn-00b4dbfc)

~~~json
{
  "source": "00b4dbfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc00`](#insn-00b4dc00)

~~~json
{
  "source": "00b4dc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc04`](#insn-00b4dc04)

~~~json
{
  "source": "00b4dc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc10`](#insn-00b4dc10)

~~~json
{
  "source": "00b4dc10",
  "target": "01125df8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125df8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dc14`](#insn-00b4dc14)

~~~json
{
  "source": "00b4dc14",
  "target": "00b4dc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc1c`](#insn-00b4dc1c)

~~~json
{
  "source": "00b4dc1c",
  "target": "00b4dc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc30`](#insn-00b4dc30)

~~~json
{
  "source": "00b4dc30",
  "target": "01125df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125df0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dc58`](#insn-00b4dc58)

~~~json
{
  "source": "00b4dc58",
  "target": "00b4dc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc84`](#insn-00b4dc84)

~~~json
{
  "source": "00b4dc84",
  "target": "01125df8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125df8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dc88`](#insn-00b4dc88)

~~~json
{
  "source": "00b4dc88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc8c`](#insn-00b4dc8c)

~~~json
{
  "source": "00b4dc8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
