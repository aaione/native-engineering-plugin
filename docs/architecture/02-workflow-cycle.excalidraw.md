# Native Engineering - 工作流循环图

```excalidraw-md
---
excalidraw-plugin: parsed
tags:
  - excalidraw
---

# Text Elements
Plan ^plan-title
Work ^work-title
Review ^review-title
Compound ^compound-title

将想法转化为
详细实现计划 ^plan-desc

研究代码库
执行开发任务
使用git worktree ^work-desc

多agent代码审查
捕获问题
识别模式 ^review-desc

文档化学习
积累知识
每次更简单 ^compound-desc

Repo Research
Framework Docs
Best Practices
Compound Recall ^plan-agents

Git Worktree
Task Tracking
Checkpoint Resume ^work-agents

DHH Reviewer
Kieran Reviewer
Security Sentinel
Performance Oracle
14+ Agents ^review-agents

Problem Analysis
Solution Extract
Category Classify
Doc Writer ^compound-agents

创建 plans/*.md ^plan-output
创建 git worktree
提交代码 ^work-output
生成审查报告
识别改进点 ^review-output
创建 docs/solutions/*.md
积累团队知识 ^compound-output

80% Planning & Review
20% Execution ^philosophy

每个工程单元
让后续工作更简单 ^philosophy2

# Layout
%%
{
  "elements": [
    {
      "type": "ellipse",
      "version": 1,
      "id": "plan-circle",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 100,
      "y": 100,
      "strokeColor": "#1e88e5",
      "backgroundColor": "#e3f2fd",
      "width": 180,
      "height": 180,
      "seed": 1,
      "groupIds": ["plan-group"],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "plan-title",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 155,
      "y": 130,
      "strokeColor": "#1e88e5",
      "backgroundColor": "transparent",
      "width": 70,
      "height": 35,
      "seed": 1,
      "groupIds": ["plan-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 28,
      "fontFamily": 1,
      "text": "Plan",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "Plan",
      "lineHeight": 1.25
    },
    {
      "type": "text",
      "version": 1,
      "id": "plan-desc",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 120,
      "y": 175,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 140,
      "height": 50,
      "seed": 1,
      "groupIds": ["plan-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 12,
      "fontFamily": 1,
      "text": "将想法转化为\n详细实现计划",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "将想法转化为\n详细实现计划",
      "lineHeight": 1.25
    },
    {
      "type": "ellipse",
      "version": 1,
      "id": "work-circle",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 520,
      "y": 100,
      "strokeColor": "#43a047",
      "backgroundColor": "#e8f5e9",
      "width": 180,
      "height": 180,
      "seed": 1,
      "groupIds": ["work-group"],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "work-title",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 570,
      "y": 130,
      "strokeColor": "#43a047",
      "backgroundColor": "transparent",
      "width": 80,
      "height": 35,
      "seed": 1,
      "groupIds": ["work-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 28,
      "fontFamily": 1,
      "text": "Work",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "Work",
      "lineHeight": 1.25
    },
    {
      "type": "text",
      "version": 1,
      "id": "work-desc",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 540,
      "y": 175,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 140,
      "height": 50,
      "seed": 1,
      "groupIds": ["work-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 12,
      "fontFamily": 1,
      "text": "研究代码库\n执行开发任务\n使用git worktree",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "研究代码库\n执行开发任务\n使用git worktree",
      "lineHeight": 1.25
    },
    {
      "type": "ellipse",
      "version": 1,
      "id": "review-circle",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 520,
      "y": 420,
      "strokeColor": "#fb8c00",
      "backgroundColor": "#fff3e0",
      "width": 180,
      "height": 180,
      "seed": 1,
      "groupIds": ["review-group"],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "review-title",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 555,
      "y": 450,
      "strokeColor": "#fb8c00",
      "backgroundColor": "transparent",
      "width": 110,
      "height": 35,
      "seed": 1,
      "groupIds": ["review-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 28,
      "fontFamily": 1,
      "text": "Review",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "Review",
      "lineHeight": 1.25
    },
    {
      "type": "text",
      "version": 1,
      "id": "review-desc",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 540,
      "y": 495,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 140,
      "height": 50,
      "seed": 1,
      "groupIds": ["review-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 12,
      "fontFamily": 1,
      "text": "多agent代码审查\n捕获问题\n识别模式",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "多agent代码审查\n捕获问题\n识别模式",
      "lineHeight": 1.25
    },
    {
      "type": "ellipse",
      "version": 1,
      "id": "compound-circle",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 100,
      "y": 420,
      "strokeColor": "#8e24aa",
      "backgroundColor": "#f3e5f5",
      "width": 180,
      "height": 180,
      "seed": 1,
      "groupIds": ["compound-group"],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "compound-title",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 115,
      "y": 450,
      "strokeColor": "#8e24aa",
      "backgroundColor": "transparent",
      "width": 150,
      "height": 35,
      "seed": 1,
      "groupIds": ["compound-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 28,
      "fontFamily": 1,
      "text": "Compound",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "Compound",
      "lineHeight": 1.25
    },
    {
      "type": "text",
      "version": 1,
      "id": "compound-desc",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 120,
      "y": 495,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 140,
      "height": 50,
      "seed": 1,
      "groupIds": ["compound-group"],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 12,
      "fontFamily": 1,
      "text": "文档化学习\n积累知识\n每次更简单",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "文档化学习\n积累知识\n每次更简单",
      "lineHeight": 1.25
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "arrow-plan-work",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 280,
      "y": 170,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 240,
      "height": 0,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "startBinding": null,
      "endBinding": null,
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [240, 0]
      ]
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "arrow-work-review",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 620,
      "y": 280,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 0,
      "height": 140,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "startBinding": null,
      "endBinding": null,
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [0, 140]
      ]
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "arrow-review-compound",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 520,
      "y": 510,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 240,
      "height": 0,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "startBinding": null,
      "endBinding": null,
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [-240, 0]
      ]
    },
    {
      "type": "arrow",
      "version": 1,
      "id": "arrow-compound-plan",
      "fillStyle": "solid",
      "strokeWidth": 3,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 180,
      "y": 420,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 0,
      "height": 140,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "startBinding": null,
      "endBinding": null,
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [0, -140]
      ]
    },
    {
      "type": "rectangle",
      "version": 1,
      "id": "center-box",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 330,
      "y": 300,
      "strokeColor": "#d32f2f",
      "backgroundColor": "#ffebee",
      "width": 140,
      "height": 100,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 1,
      "id": "philosophy",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 340,
      "y": 315,
      "strokeColor": "#d32f2f",
      "backgroundColor": "transparent",
      "width": 120,
      "height": 32,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 13,
      "fontFamily": 1,
      "text": "80% Planning\n     & Review\n20% Execution",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "80% Planning & Review\n20% Execution",
      "lineHeight": 1.25
    },
    {
      "type": "text",
      "version": 1,
      "id": "philosophy2",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 0,
      "opacity": 100,
      "angle": 0,
      "x": 340,
      "y": 360,
      "strokeColor": "#424242",
      "backgroundColor": "transparent",
      "width": 120,
      "height": 28,
      "seed": 1,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "boundElements": [],
      "updated": 1,
      "link": null,
      "locked": false,
      "fontSize": 11,
      "fontFamily": 1,
      "text": "每个工程单元\n让后续工作更简单",
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": null,
      "originalText": "每个工程单元\n让后续工作更简单",
      "lineHeight": 1.25
    }
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
%%
```
