<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2023-05-16T12:00:00.000Z" agent="5.0 (Windows)">
  <diagram name="Page-1" id="your-diagram-id">
    <mxGraphModel dx="1060" dy="500" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Course -->
        <mxCell id="course" value="Course" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="220" y="80" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="courseCode" value="- course_code: string" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="30" width="150" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="courseName" value="- course_name: string" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="60" width="150" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="courseProfessor" value="- professor: Professor" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="90" width="150" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="students" value="- students: list&lt;Student&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="120" width="150" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="addStudent" value="+ add_student(student: Student)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="160" width="150" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="removeStudent" value="+ remove_student(student: Student)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="course">
          <mxGeometry x="30" y="190" width="150" height="20" as="geometry" />
        </mxCell>
    <!-- Professor -->
    <mxCell id="professor" value="Professor" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="1">
      <mxGeometry x="220" y="300" width="120" height="80" as="geometry" />
    </mxCell>
    
    <mxCell id="professorName" value="- name: string" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="professor">
      <mxGeometry x="30" y="30" width="150" height="20" as="geometry" />
    </mxCell>
    
    <mxCell id="coursesTaught" value="- courses_taught: list&lt;Course&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="professor">
      <mxGeometry x="30" y="60" width="150" height="20" as="geometry" />
    </mxCell>
    
    <mxCell id="addCourse" value="+ add_course(course: Course)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="professor">
      <mxGeometry x="30" y="120" width="150" height="20" as="geometry" />
    </mxCell>
    
    <mxCell id="removeCourse" value="+ remove_course(course: Course)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="professor">
      <mxGeometry x="30" y="150" width="150" height="20" as="geometry" />
    </mxCell>
    
    <!-- Student -->
    <mxCell id="student" value="Student" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="1">
      <mxGeometry x="220" y="480" width="120" height="80" as="geometry" />
    </mxCell>
    
    <mxCell id="studentName" value="- name: string" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="student">
      <mxGeometry x="30" y="30" width="150" height="20" as="geometry" />
    </mxCell>
    
    <mxCell id="coursesEnrolled" value="- courses_enrolled: list&lt;Course&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="student">
      <mxGeometry x="30" y="60" width="150" height="20" as="geometry" />
    </mxCell>
    
    <mxCell id="enrollCourse" value="+ enroll_course(course: Course)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="student">
      <mxGeometry x="30" y="120" width="150" height="20" as="geometry"/>
    </mxCell>
    <mxCell id="dropCourse" value="+ drop_course(course: Course)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;" vertex="1" parent="student">
      <mxGeometry x="30" y="150" width="150" height="20" as="geometry" />
    </mxCell>
    
    <!-- Relationships -->
    <mxCell id="course-professor" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="course" target="professor">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    
    <mxCell id="course-students" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="course" target="students">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    
    <mxCell id="professor-coursesTaught" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="professor" target="coursesTaught">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    
    <mxCell id="student-coursesEnrolled" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="student" target="coursesEnrolled">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    
  </root>
</mxGraphModel>
 </diagram>
</mxfile>

